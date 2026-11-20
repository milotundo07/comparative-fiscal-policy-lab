from __future__ import annotations

from dataclasses import dataclass

from fiscal_lab.models import FiscalRegime, MineProject


@dataclass(frozen=True)
class SimulationResult:
    """Annual fiscal and simplified investor outcomes for one scenario."""

    regime_name: str
    gross_revenue_usd: float
    operating_costs_usd: float
    depreciation_usd: float
    operating_profit_before_fiscal_charges_usd: float
    royalty_usd: float
    profit_after_royalty_before_windfall_usd: float
    normal_return_allowance_usd: float
    windfall_tax_base_usd: float
    windfall_tax_usd: float
    cit_taxable_profit_usd: float
    cit_usd: float
    government_revenue_usd: float
    accounting_profit_after_tax_usd: float
    operating_cash_surplus_after_tax_usd: float
    effective_government_take_on_positive_profit: float | None


def simulate(project: MineProject, regime: FiscalRegime) -> SimulationResult:
    """Calculate a transparent annual tax simulation for one mine project.

    Simplifications:
    - royalty is charged on gross sales revenue;
    - the windfall base is profit after royalty less a normal return allowance;
    - CIT is charged on a positive base after the configured deductions;
    - tax losses are not carried forward;
    - there is no behavioural response or time-value-of-money calculation.
    """

    gross_revenue = project.production_tonnes * project.copper_price_usd_per_tonne
    operating_costs = project.production_tonnes * project.operating_cost_usd_per_tonne
    operating_profit = gross_revenue - operating_costs - project.annual_depreciation_usd

    royalty = gross_revenue * regime.royalty_rate
    profit_after_royalty = operating_profit - royalty

    normal_return_allowance = project.invested_capital_usd * regime.normal_return_rate
    windfall_base = max(0.0, profit_after_royalty - normal_return_allowance)
    windfall_tax = windfall_base * regime.windfall_tax_rate

    cit_base = operating_profit
    if regime.royalty_deductible_for_cit:
        cit_base -= royalty
    if regime.windfall_tax_deductible_for_cit:
        cit_base -= windfall_tax
    cit_base = max(0.0, cit_base)
    cit = cit_base * regime.cit_rate

    government_revenue = royalty + windfall_tax + cit
    accounting_profit_after_tax = operating_profit - government_revenue
    operating_cash_surplus_after_tax = (
        gross_revenue - operating_costs - government_revenue
    )

    effective_take = (
        government_revenue / operating_profit if operating_profit > 0 else None
    )

    return SimulationResult(
        regime_name=regime.name,
        gross_revenue_usd=gross_revenue,
        operating_costs_usd=operating_costs,
        depreciation_usd=project.annual_depreciation_usd,
        operating_profit_before_fiscal_charges_usd=operating_profit,
        royalty_usd=royalty,
        profit_after_royalty_before_windfall_usd=profit_after_royalty,
        normal_return_allowance_usd=normal_return_allowance,
        windfall_tax_base_usd=windfall_base,
        windfall_tax_usd=windfall_tax,
        cit_taxable_profit_usd=cit_base,
        cit_usd=cit,
        government_revenue_usd=government_revenue,
        accounting_profit_after_tax_usd=accounting_profit_after_tax,
        operating_cash_surplus_after_tax_usd=operating_cash_surplus_after_tax,
        effective_government_take_on_positive_profit=effective_take,
    )
