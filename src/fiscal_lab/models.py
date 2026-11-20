from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


def _validate_non_negative(name: str, value: float) -> None:
    if not isfinite(value) or value < 0:
        raise ValueError(f"{name} must be a finite, non-negative number.")


def _validate_rate(name: str, value: float) -> None:
    if not isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be between 0 and 1.")


@dataclass(frozen=True)
class MineProject:
    """Annual operating assumptions for one simplified mining project."""

    production_tonnes: float
    copper_price_usd_per_tonne: float
    operating_cost_usd_per_tonne: float
    annual_depreciation_usd: float
    invested_capital_usd: float

    def __post_init__(self) -> None:
        _validate_non_negative("production_tonnes", self.production_tonnes)
        _validate_non_negative(
            "copper_price_usd_per_tonne", self.copper_price_usd_per_tonne
        )
        _validate_non_negative(
            "operating_cost_usd_per_tonne", self.operating_cost_usd_per_tonne
        )
        _validate_non_negative("annual_depreciation_usd", self.annual_depreciation_usd)
        _validate_non_negative("invested_capital_usd", self.invested_capital_usd)


@dataclass(frozen=True)
class FiscalRegime:
    """Tax parameters for a single annual project-level scenario.

    The windfall tax is applied to profit after royalty and above a normal
    return allowance on invested capital. Deductibility flags determine the
    simplified CIT base; they do not represent a statement of any country's law.
    """

    name: str
    royalty_rate: float
    cit_rate: float
    windfall_tax_rate: float = 0.0
    normal_return_rate: float = 0.10
    royalty_deductible_for_cit: bool = True
    windfall_tax_deductible_for_cit: bool = True

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must not be empty.")
        _validate_rate("royalty_rate", self.royalty_rate)
        _validate_rate("cit_rate", self.cit_rate)
        _validate_rate("windfall_tax_rate", self.windfall_tax_rate)
        _validate_non_negative("normal_return_rate", self.normal_return_rate)
