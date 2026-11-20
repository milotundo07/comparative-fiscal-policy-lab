# First model specification

## Purpose

This note documents the first annual, single-project fiscal simulation. It is a transparent accounting model for scenario analysis. It is not a forecast, a complete mining tax model, a replication of IMF FARI or an estimate of the causal effect of a tax reform.

## Inputs

For each project-year:

- Q: copper production, in tonnes;
- P: copper sale price, in USD per tonne;
- C: operating cost, in USD per tonne;
- D: annual depreciation or capital-allowance proxy, in USD;
- K: invested capital, in USD.

For each fiscal regime:

- r: royalty rate on gross sales revenue;
- t: corporate income tax rate;
- w: windfall-tax rate;
- h: normal-return allowance as a share of invested capital;
- d_r: whether royalties are deductible for CIT;
- d_w: whether windfall tax is deductible for CIT.

Rates are expressed as decimals in the code: 0.05 means 5%.

## Equations

Gross revenue: R = Q × P

Operating costs: O = Q × C

Operating profit before fiscal charges: Π = R − O − D

Royalty on gross revenue: Royalty = R × r

Profit after royalty, before windfall tax: Π_r = Π − Royalty

Normal-return allowance: A = K × h

Windfall-tax base: max(0, Π_r − A)

Windfall tax: Windfall base × w

Simplified CIT taxable profit:

    CIT base = max(0, Π − d_r × Royalty − d_w × Windfall tax)

    CIT = CIT base × t

Here d_r and d_w equal 1 when the relevant charge is deductible and 0 otherwise.

Government revenue = Royalty + Windfall tax + CIT

Simplified investor accounting profit after tax = Π − Royalty − Windfall tax − CIT.

The application also reports an operating cash surplus after tax. It subtracts operating costs and modelled taxes from sales revenue but does not subtract capital expenditure, debt service or working-capital changes. It should not be interpreted as free cash flow.

## Key modelling choices

1. The royalty is modelled as an ad valorem charge on gross sales revenue.
2. The windfall tax is an excess-profit tax based on profit after royalty and above a normal-return allowance on invested capital. It is not a price-triggered tax.
3. The windfall tax base is calculated after royalty. This is an explicit analytical convention.
4. Royalty and windfall-tax deductibility for CIT are configurable assumptions.
5. CIT is charged only on a positive simplified taxable-profit base.
6. The normal-return allowance is a user-specified rate multiplied by invested capital. The model does not yet define how the capital base is valued, depreciated or updated over time.
7. The model uses annual aggregates and does not distinguish between mine ownership structures or corporate groups.

These choices are deliberately visible and should be reviewed against the legislation before any scenario is described as a simulation of Zambia's actual tax system.

## Limitations

The model currently omits tax-loss carry-forwards, ring-fencing, detailed capital allowances, interest deductions, debt-equity structures, withholding taxes, VAT, customs duties, hedging, transfer pricing, related-party transactions, state participation, fiscal stability clauses, mine closure costs, project development timelines, discounting, exchange-rate effects and strategic behavioural responses.

The model also assumes that production, unit costs, depreciation and invested capital do not respond to the tax regime. It therefore cannot estimate investment deterrence, entry, exit, production changes or wider domestic economic effects.

## Interpretation

The difference between two scenarios is a mechanical result conditional on the inputs and equations. It is not evidence that a government would collect that amount in practice.

A higher modelled government revenue figure does not establish that the policy is welfare-improving. Nor does the model currently estimate employment, local procurement, domestic ownership, productivity, diversification or distributional effects.

## Validation plan

Before using the model for substantive Zambia analysis:

1. Verify the applicable law and effective dates for each tax instrument.
2. Check the tax base and deductibility treatment against legislation and authoritative guidance.
3. Compare the model's outputs with worked examples or established resource-tax models where possible.
4. Test edge cases, including losses, price shocks, low output and changes in the capital base.
5. Record data source, period, unit, currency, transformation and uncertainty for every empirical input.
6. Obtain review from a researcher with mining-tax and public-finance expertise.
