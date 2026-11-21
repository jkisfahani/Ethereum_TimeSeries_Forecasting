# Ethereum Daily Transaction Counts — Data Provenance

## Dataset information

- Dataset: Ethereum daily transaction counts
- Source: Google BigQuery
- Source table: `bigquery-public-data.goog_blockchain_ethereum_mainnet.transactions`
- Original filename: `ethereum_daily_transaction_counts.csv`
- Location: `data/raw/`
- Date coverage: 2015-10-01 to 2026-11-17
- Extraction date: Not independently verified
- Windows file creation time: 2026-11-18 19:28:50
- Windows last modified time: 2026-11-18 19:29:02
- File size: 74,790 bytes

## File integrity

- Checksum algorithm: SHA-256
- SHA-256: `D61E28F90F53A7A53091B6DE5C55553727CA95D081746EEFD7B7B47B2C9DF63E`

## Reproducibility notes

The CSV is retained as the original exported dataset used in the Ethereum time-series forecasting project.

The original file should not be modified. Any cleaning, transformation, or feature engineering should be performed on separate derived datasets.

The SQL extraction query is preserved separately in `sql/daily_transaction_counts.sql`.

The SQL file is documented as a reconstruction and should not be represented as the verified original query unless that can be independently established.

## Verification

To recalculate the checksum on Windows PowerShell, run:

`Get-FileHash "data/raw/ethereum_daily_transaction_counts.csv" -Algorithm SHA256`
