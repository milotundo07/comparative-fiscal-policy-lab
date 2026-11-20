import pytest

from fiscal_lab.models import FiscalRegime, MineProject
from fiscal_lab.tax import simulate


def sample_project() -> MineProject:
    return MineProject(
        production_tonnes=100,
        copper_price_usd_per_tonne=1_000,
        operating_cost_usd_per_tonne=400,
        annual_depreciation_usd=10_000,
        invested_capital_usd=200_000,
    )


def test_windfall_tax_and_deductible_cit_calculation() -> None:
    regime = FiscalRegime(
        name="Test reform",
        royalty_rate=0.05,
        cit_rate=0.25,
        windfall_tax_rate=0.20,
        normal_return_rate=0.10,
        royalty_deductible_for_cit=True,
        windfall_tax_deductible_for_cit=True,
    )
    result = simulate(sample_project(), regime)

    assert result.gross_revenue_usd == pytest.approx(100_000)
    assert result.operating_costs_usd == pytest.approx(40_000)
    assert result.operating_profit_before_fiscal_charges_usd == pytest.approx(50_000)
    assert result.royalty_usd == pytest.approx(5_000)
    assert result.normal_return_allowance_usd == pytest.approx(20_000)
    assert result.windfall_tax_base_usd == pytest.approx(25_000)
    assert result.windfall_tax_usd == pytest.approx(5_000)
    assert result.cit_taxable_profit_usd == pytest.approx(40_000)
    assert result.cit_usd == pytest.approx(10_000)
    assert result.government_revenue_usd == pytest.approx(20_000)
    assert result.accounting_profit_after_tax_usd == pytest.approx(30_000)


def test_non_deductible_windfall_tax_does_not_reduce_cit_base() -> None:
    regime = FiscalRegime(
        name="Non-deductible reform",
        royalty_rate=0.05,
        cit_rate=0.25,
        windfall_tax_rate=0.20,
        normal_return_rate=0.10,
        royalty_deductible_for_cit=True,
        windfall_tax_deductible_for_cit=False,
    )
    result = simulate(sample_project(), regime)
    assert result.cit_taxable_profit_usd == pytest.approx(45_000)
    assert result.cit_usd == pytest.approx(11_250)


def test_royalty_is_charged_even_when_project_makes_a_loss() -> None:
    project = MineProject(
        production_tonnes=100,
        copper_price_usd_per_tonne=300,
        operating_cost_usd_per_tonne=500,
        annual_depreciation_usd=10_000,
        invested_capital_usd=200_000,
    )
    regime = FiscalRegime(
        name="Loss-making project",
        royalty_rate=0.05,
        cit_rate=0.30,
        windfall_tax_rate=0.25,
    )
    result = simulate(project, regime)

    assert result.royalty_usd == pytest.approx(1_500)
    assert result.windfall_tax_usd == pytest.approx(0)
    assert result.cit_usd == pytest.approx(0)
    assert result.effective_government_take_on_positive_profit is None


def test_zero_production_produces_no_revenue_or_taxes() -> None:
    project = MineProject(
        production_tonnes=0,
        copper_price_usd_per_tonne=9_000,
        operating_cost_usd_per_tonne=6_000,
        annual_depreciation_usd=0,
        invested_capital_usd=500_000_000,
    )
    regime = FiscalRegime(
        name="Zero output",
        royalty_rate=0.05,
        cit_rate=0.30,
        windfall_tax_rate=0.25,
    )
    result = simulate(project, regime)

    assert result.gross_revenue_usd == pytest.approx(0)
    assert result.government_revenue_usd == pytest.approx(0)


@pytest.mark.parametrize("rate", [-0.01, 1.01])
def test_invalid_tax_rates_are_rejected(rate: float) -> None:
    with pytest.raises(ValueError):
        FiscalRegime(name="Invalid", royalty_rate=rate, cit_rate=0.30)


def test_negative_project_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        MineProject(
            production_tonnes=-1,
            copper_price_usd_per_tonne=9_000,
            operating_cost_usd_per_tonne=6_000,
            annual_depreciation_usd=0,
            invested_capital_usd=1,
        )
