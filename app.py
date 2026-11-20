from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent / "src"))

from fiscal_lab.models import FiscalRegime, MineProject
from fiscal_lab.tax import simulate

st.set_page_config(page_title="Zambia Copper Tax Simulator", layout="wide")
st.title("Zambia Copper Tax Simulator")
st.caption("Comparative Fiscal Policy Lab · First research prototype")

st.warning(
    "Illustrative model only. The starting values are synthetic placeholders, "
    "not verified Zambian statutory tax rates, company accounts or forecasts. "
    "Do not interpret the outputs as estimates of Zambia's actual tax take."
)

with st.sidebar:
    st.header("1. Mine and market assumptions")
    production = st.number_input(
        "Annual copper production (tonnes)", min_value=0.0,
        value=100_000.0, step=5_000.0,
    )
    copper_price = st.number_input(
        "Copper price (USD per tonne)", min_value=0.0,
        value=9_000.0, step=250.0,
    )
    operating_cost = st.number_input(
        "Operating cost (USD per tonne)", min_value=0.0,
        value=6_000.0, step=250.0,
    )
    depreciation = st.number_input(
        "Annual depreciation / capital allowance proxy (USD)",
        min_value=0.0, value=100_000_000.0, step=5_000_000.0,
    )
    invested_capital = st.number_input(
        "Invested capital (USD)", min_value=0.0,
        value=500_000_000.0, step=25_000_000.0,
    )

    st.header("2. Reference regime")
    reference_royalty = st.slider(
        "Royalty rate", 0.0, 0.20, 0.05, 0.005, key="ref_royalty"
    )
    reference_cit = st.slider(
        "CIT rate", 0.0, 0.50, 0.30, 0.01, key="ref_cit"
    )
    reference_royalty_deductible = st.checkbox(
        "Royalty deductible for CIT", value=True, key="ref_royalty_deductible"
    )

    st.header("3. Reform scenario")
    reform_royalty = st.slider("Reform royalty rate", 0.0, 0.20, 0.05, 0.005)
    reform_cit = st.slider("Reform CIT rate", 0.0, 0.50, 0.30, 0.01)
    windfall_rate = st.slider("Windfall tax rate", 0.0, 0.75, 0.25, 0.01)
    normal_return = st.slider(
        "Normal return allowance on invested capital", 0.0, 0.30, 0.10, 0.01
    )
    reform_royalty_deductible = st.checkbox(
        "Reform royalty deductible for CIT", value=True
    )
    windfall_deductible = st.checkbox(
        "Windfall tax deductible for CIT", value=True
    )

project = MineProject(
    production_tonnes=production,
    copper_price_usd_per_tonne=copper_price,
    operating_cost_usd_per_tonne=operating_cost,
    annual_depreciation_usd=depreciation,
    invested_capital_usd=invested_capital,
)
reference = FiscalRegime(
    name="Reference regime",
    royalty_rate=reference_royalty,
    cit_rate=reference_cit,
    royalty_deductible_for_cit=reference_royalty_deductible,
)
reform = FiscalRegime(
    name="Windfall reform",
    royalty_rate=reform_royalty,
    cit_rate=reform_cit,
    windfall_tax_rate=windfall_rate,
    normal_return_rate=normal_return,
    royalty_deductible_for_cit=reform_royalty_deductible,
    windfall_tax_deductible_for_cit=windfall_deductible,
)

reference_result = simulate(project, reference)
reform_result = simulate(project, reform)
revenue_delta = (
    reform_result.government_revenue_usd - reference_result.government_revenue_usd
)
profit_delta = (
    reform_result.accounting_profit_after_tax_usd
    - reference_result.accounting_profit_after_tax_usd
)

st.subheader("Headline comparison")
metric_cols = st.columns(3)
metric_cols[0].metric(
    "Government revenue · reference",
    f"USD {reference_result.government_revenue_usd:,.0f}",
)
metric_cols[1].metric(
    "Government revenue · reform",
    f"USD {reform_result.government_revenue_usd:,.0f}",
    delta=f"USD {revenue_delta:,.0f} vs reference",
)
metric_cols[2].metric(
    "Investor after-tax profit · reform",
    f"USD {reform_result.accounting_profit_after_tax_usd:,.0f}",
    delta=f"USD {profit_delta:,.0f} vs reference",
)

st.caption(
    "All monetary values are annual USD. Investor profit is a simplified "
    "accounting measure after the modelled taxes, before financing costs."
)

st.subheader("Fiscal breakdown")
rows = []
for result in (reference_result, reform_result):
    rows.append({
        "Scenario": result.regime_name,
        "Gross revenue": result.gross_revenue_usd,
        "Royalty": result.royalty_usd,
        "Windfall tax": result.windfall_tax_usd,
        "CIT": result.cit_usd,
        "Government revenue": result.government_revenue_usd,
        "Investor after-tax profit": result.accounting_profit_after_tax_usd,
        "CIT taxable profit": result.cit_taxable_profit_usd,
    })

breakdown = pd.DataFrame(rows).set_index("Scenario")
st.dataframe(breakdown.style.format("USD {:,.0f}"), use_container_width=True)

chart_left, chart_right = st.columns(2)
with chart_left:
    st.subheader("Government revenue by instrument")
    fiscal_components = pd.DataFrame(
        {
            "Royalty": [reference_result.royalty_usd, reform_result.royalty_usd],
            "Windfall tax": [
                reference_result.windfall_tax_usd, reform_result.windfall_tax_usd
            ],
            "CIT": [reference_result.cit_usd, reform_result.cit_usd],
        },
        index=["Reference regime", "Windfall reform"],
    )
    st.bar_chart(fiscal_components)

with chart_right:
    st.subheader("Investor after-tax accounting profit")
    investor_profit = pd.DataFrame(
        {
            "After-tax profit": [
                reference_result.accounting_profit_after_tax_usd,
                reform_result.accounting_profit_after_tax_usd,
            ]
        },
        index=["Reference regime", "Windfall reform"],
    )
    st.bar_chart(investor_profit)

st.subheader("Copper-price sensitivity")
st.caption(
    "Only the copper price changes. Production, costs, capital, depreciation "
    "and tax parameters remain fixed."
)
price_points = sorted({
    max(0.0, copper_price * factor)
    for factor in (0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40)
})
sensitivity_rows = []
for price in price_points:
    price_project = MineProject(
        production_tonnes=production,
        copper_price_usd_per_tonne=price,
        operating_cost_usd_per_tonne=operating_cost,
        annual_depreciation_usd=depreciation,
        invested_capital_usd=invested_capital,
    )
    ref_at_price = simulate(price_project, reference)
    reform_at_price = simulate(price_project, reform)
    sensitivity_rows.append({
        "Copper price (USD/t)": price,
        "Reference regime": ref_at_price.government_revenue_usd,
        "Windfall reform": reform_at_price.government_revenue_usd,
    })

sensitivity = pd.DataFrame(sensitivity_rows).set_index("Copper price (USD/t)")
st.line_chart(sensitivity)

st.download_button(
    "Download scenario results (CSV)",
    data=breakdown.to_csv().encode("utf-8"),
    file_name="zambia_copper_tax_scenarios.csv",
    mime="text/csv",
)

with st.expander("Interpretation and limitations"):
    st.markdown(
        """
        - The windfall tax applies to profit above a normal-return allowance on
          invested capital. It is not a price-triggered tax.
        - The windfall-tax base is calculated after the royalty, as an explicit
          modelling convention.
        - CIT applies only to a positive simplified taxable-profit base.
          Loss carry-forwards and detailed tax depreciation are not modelled.
        - The reform scenario is not a recommendation and is not calibrated to
          verified Zambian law or company-level data.
        - The model does not predict changes in investment, production,
          financing, transfer pricing or mine life.
        - Higher modelled government revenue does not by itself demonstrate
          higher domestic investment, diversification or development outcomes.
        """
    )

st.caption(
    "Comparative Fiscal Policy Lab · Prototype 0.1.0 · "
    "See docs/MODEL.md for equations and assumptions."
)
