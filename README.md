# Comparative Fiscal Policy Lab

An open-source research platform for comparative fiscal policy analysis, mining tax simulation and economic policy evaluation. The first case study is Zambia's copper sector.

## Current milestone: Zambia Copper Tax Simulator

The first prototype is a transparent annual, single-project fiscal model. It compares a user-defined reference regime with a user-defined reform scenario.

It includes:
- copper production, price, operating costs, depreciation and invested capital;
- ad valorem royalties on gross revenue;
- corporate income tax (CIT) on a simplified taxable-profit base;
- an excess-profit tax on returns above a normal-return allowance on invested capital;
- configurable deductibility of royalties and windfall tax for CIT;
- government revenue and investor-profit comparisons;
- copper-price sensitivity analysis;
- unit tests for the core tax calculations.

**Important:** default inputs and tax rates are illustrative placeholders. They are not Zambia's statutory tax rates, mine-level observations or forecasts. No official Zambia dataset has yet been integrated. The application does not currently estimate causal policy effects.

## Run locally

Python 3.11 or later is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Run the tests:

```bash
pip install -e ".[dev]"
pytest
```

## Model boundaries

The first version is an annual, single-project accounting model. It is designed to make assumptions visible and calculations reproducible, not to replicate a complete mining fiscal regime.

It does not yet model tax-loss carry-forwards, ring-fencing, detailed tax depreciation, financing costs, interest deductibility, withholding taxes, VAT, customs duties, transfer pricing, fiscal stability clauses, state equity participation, mine development timelines, closure costs, discounting or behavioural responses.

See `docs/MODEL.md` for equations, assumptions and limitations.

## Research principles

1. Separate observed data, sourced legal parameters and illustrative assumptions.
2. Record the source, unit, period, geography, vintage and transformation for every empirical input.
3. Distinguish mechanical fiscal simulations from causal estimates of historical reforms.
4. Report uncertainty and sensitivity rather than presenting a single projection as a prediction.
5. Do not label a scenario as the current law of a country until the relevant legislation and effective dates have been checked.

## Planned development

1. Validate the fiscal engine and add explicit regime components.
2. Build a source register and reproducible data-ingestion pipeline.
3. Document Zambia's applicable legal regime and collect mine- and sector-level data where available.
4. Assess the suitability of the DRC, Peru, Chile and other potential comparators using transparent indicators.
5. Evaluate historical reforms only where a credible comparison group and identifying assumptions are defensible.
6. Expose assumptions, results, sources and limitations through an interactive research interface.

## Sources and data

`data/source_register.csv` is the starting register for datasets, legal documents and other evidence. No external dataset is bundled at this stage. Check source licences and terms before adding or redistributing data.

## Licence

The code is released under the MIT License. This does not change the licences or terms governing third-party datasets, documents or APIs.
