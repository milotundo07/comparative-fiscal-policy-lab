# Fiscal model 0.2

## Annual accounting

All prices are nominal USD per metric tonne and rates are fractions in the engine. Quantity is copper sold. The original Python field name `production_tonnes` is retained for compatibility. Sales revenue is quantity times sale price. Operating costs are quantity times unit operating cost.

The Zambia 2024 reference uses 30% mining CIT and a deductible copper royalty. Marginal royalty rates are 4% on the first USD 4,000/t of norm price, 6.5% on the next 1,000, 8.5% on the next 2,000 and 10% above 7,000. At USD 9,000/t the royalty is USD 595/t. The law uses a monthly reference price and monthly quantities sold. Upload the 12 monthly quantities and norm prices to calculate and sum monthly liabilities. Without a monthly file, the bands apply to a single annual norm price. Because the bands are progressive, annual aggregation can differ from the sum of monthly liabilities. The mine's realised sale price is a separate input. The model assumes the royalty is paid within the charge year. The custom regime uses a flat rate on sales revenue.

Current-year CIT profit is sales less operating costs and the tax allowance, less royalty and any additional tax when each is deductible. Available CIT losses offset at most the configured fraction of positive taxable profit. Annual mode assumes zero opening losses. CIT applies to positive profit after losses. Book depreciation is separate from the tax allowance. Government revenue sums the three modelled taxes. Accounting profit subtracts book depreciation and taxes. Cash flow subtracts operating expenses, taxes and capex. It excludes financing, working capital and terminal values.

## Alternative reforms

The normal-return instrument applies the rate to positive book profit after royalty and the configured normal return on invested capital.

For the indexed-price instrument, just one reference copper price is chosen. Each period's threshold is the fixed base price multiplied by the ratio of the period inflation index to the base index. The price increment is the positive difference between sale price and indexed threshold. The counterfactual norm price equals the actual norm price less the same increment, floored at zero. For a flat royalty, the counterfactual uses the lower sales revenue directly.

The price-attributable gain is the price increment times tonnes sold, less any increase in the royalty caused by that increment. Eligible profit equals actual revenue less operating costs, tax allowance and royalty. The taxable excess is the smaller of eligible profit and price-attributable gain, floored at zero. This convention exempts loss years and prevents taxing more than either the price gain or positive fiscal profit. The 20% rate and deductibility are editable research assumptions. There is no separate windfall loss pool or uplift. Capex recovery enters through the allowance. The model uses the chosen inflation series as supplied, with no automatic index updates or repricing of the reference year.

## Sentinel 2024

The illustrative reconstruction pairs the reported 222,791 tonnes of copper sold with USD 1,945m of copper revenue. Trident's USD 2,196m total includes USD 251m of nickel revenue. The price proxy divides reported copper revenue by tonnes sold. The USD 4.15/lb annual LME average converts using 2,204.62262185 lb per metric tonne. The operating-cost proxy is the USD 1,285m Sentinel cost of sales less USD 295m book depreciation and USD 133m royalties, or USD 857m before dividing by tonnes sold. This removes the charges the simulator applies separately. The USD 195m capex input covers reported sustaining capex and deferred stripping. Total capex may differ. The standalone tax allowance and invested capital are editable assumptions. Results are modelled outcomes and cannot be reconciled directly to the operator's tax return. See the data register for the company disclosure and legal sources.

## Project life

Upload consecutive years using the example CSV columns. Schedules can cover construction and operations. Each capex cohort receives straight-line fiscal allowances beginning in its spending year. Unused CIT losses carry forward with no age limit, subject to the input annual offset cap. Opening losses and historical asset vintages are zero at the start of the schedule. The scenario does not claim to apply the full Zambian capital allowance, expiry or ring-fencing rules. The published NPV discounts annual government receipts and unlevered investor cash flows at the selected common nominal USD rate, assuming end-year flows. Operating, production, capex and price schedules are identical across regimes. The schedule can represent closure-period spending as cash outflow, without separate fiscal rules for closure.

## Chile comparison

The Chile view compares mineral royalties for a large copper operator under Law 21.591 arts. 2, 3 and 8. It calculates the 1% sales component and the 8%–26% margin component, applying the 45.5% or 46.5% ceiling with the SII Circular 3/2024 formulas. The tests replicate SII Annexes 6 and 7. The app assumes mining operating revenue equals copper sales, and asks for the statutory sales equivalent, RIOMA before royalty and the income tax base before royalty. The annual copper tonnage and operating margin serve only as editable starting proxies. The eligibility input represents the statutory sales average and aggregation that the user must establish. The app excludes other operator classes and does not calculate Chile's income taxes as separate receipts. The two royalty totals cannot rank full fiscal burdens.

The model simulates mechanical tax and cash-flow outcomes. Investment decisions, production responses and development outcomes require separate evidence and modelling.
