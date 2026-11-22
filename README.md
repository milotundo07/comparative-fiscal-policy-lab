# Comparative Fiscal Policy Lab

A Streamlit research prototype for comparing copper mining taxes. Version 0.2 includes an annual Zambia 2024 proxy, an indexed-price reform, a normal-return alternative, a multi-year cash-flow model and a comparison with Chile's royalty for large copper operators.

## Run locally

Python 3.11 or 3.12 is supported.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1`.

## Use the simulator

- **Annual comparison** compares a synthetic mine or the Sentinel 2024 illustrative reconstruction under the selected reference and reform. Set the sale price and upload monthly Zambia royalty inputs or use an annual norm-price proxy.
- **Project life** starts with a synthetic multi-year schedule. Download the template, edit the assumptions and upload the CSV to see yearly taxes, loss balances, cash flows and their present values.
- **Chile comparison** compares Zambia's royalty with Chile's ad valorem and margin components, including the Chilean tax ceiling. See the model specification for the rules excluded from each proxy.
- **Sources and method** records the distinction between cited legal rules, company figures, transformations and research assumptions.

Download the JSON record to keep the precise inputs, regime configuration, units, sources, model version and results. CSV downloads give the output tables for further analysis. See [model specifications](docs/MODEL.md) and the [data register](data/source_register.csv).

## Tests

```bash
python -m pip install -r requirements.txt -e ".[dev]"
python -m pytest -q
```

The tests cover accounting identities, statutory royalty band arithmetic, both additional tax bases, loss carry-forward, discounting and Streamlit scenario navigation. GitHub Actions runs them on Python 3.11 and 3.12.

## Licence

The code uses the MIT License. Third-party sources have their own terms.
