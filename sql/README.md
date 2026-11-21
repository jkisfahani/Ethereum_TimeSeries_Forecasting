# BigQuery SQL and data extraction

## Files

- `daily_transaction_counts.sql`: Standard SQL query that aggregates Ethereum Mainnet transactions into one record per UTC calendar day.

## Source

The query reads:

`bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions`

The date window is inclusive from **2015-10-01** through **2026-11-17**. The timestamp predicate uses a half-open interval ending at `2026-11-18 00:00:00+00`, which includes every timestamp on 17 November and avoids end-of-day boundary ambiguity.

## Query behaviour

1. Converts `block_timestamp` to a UTC calendar date.
2. Counts source rows with `COUNT(*)` for each date.
3. Generates a complete daily calendar for the study period.
4. Left-joins the counts to that calendar and fills any absent dates with zero.
5. Returns two columns, ordered by date:
   - `block_date` (DATE)
   - `daily_transaction_count` (integer count)

The query uses Standard SQL. In the BigQuery editor, use the processing location compatible with the source dataset.

## Reproducing the dataset

1. Open the BigQuery SQL workspace in Google Cloud.
2. Open `daily_transaction_counts.sql` from this repository and run it as a Standard SQL query.
3. Export the query result to CSV.
4. Preserve the exported CSV unchanged as the raw extraction artifact, and record the extraction date, query revision/commit, and export filename in the project data documentation.
5. Compare the exported row count and date range with the study dataset before using it in the notebook. The expected output is 4,066 rows, from 2015-10-01 through 2026-11-17.
6. Run the notebook's cleaning and modelling workflow against the verified CSV.

## Important provenance note

The SQL file is a **documented reconstruction of the daily aggregation**, not a verified byte-for-byte copy of the exact original query that produced the historical processed CSV. The original executed query was not preserved in the available project history. Do not describe this reconstruction as the exact original extraction query unless its output has been checked against the archived source CSV and the match has been documented.

For strict reproducibility, retain the original query text and the exact exported source CSV together with their dates and checksums whenever they are available. If the reconstructed query produces different daily counts, investigate the source table version, date boundaries, timestamp convention, and aggregation logic before treating the outputs as equivalent.
