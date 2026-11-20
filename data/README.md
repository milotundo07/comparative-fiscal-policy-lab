# Data governance

No empirical country or company dataset is bundled with the first prototype. The app's default values are synthetic inputs used only to demonstrate the calculation engine.

## Source register

Record every dataset, legal instrument and document in source_register.csv. Include the organisation and exact title, variables extracted, geography and period coverage, frequency and original unit, URL and access date, licence or terms of use, transformations, exclusions and known limitations, quality status and verification date.

## Data handling rules

1. Preserve the original downloaded file separately from cleaned and transformed data.
2. Never overwrite source values during cleaning.
3. Keep a reproducible script for each transformation.
4. Record the currency, price basis, unit and reference year.
5. Distinguish national-sector data from individual mine or company data.
6. Do not treat missing values as zero.
7. Check whether data are comparable across countries before calculating similarity scores.
8. Check licences and terms before committing or redistributing data.
9. Do not commit confidential company information, personal data, API keys or credentials.

A source is not considered verified merely because it appears in an international database. Its definition, coverage, vintage and methodological notes must also be checked.
