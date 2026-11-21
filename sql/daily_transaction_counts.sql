-- Reproducible daily Ethereum transaction-count aggregation.
-- Source: Google Cloud Blockchain Analytics, Ethereum Mainnet transactions.
-- This is a documented reconstruction of the aggregation used for this project;
-- it is not represented as the exact original query unless its output is checked
-- against the archived CSV file.
--
-- Date convention: UTC calendar days.
-- Inclusive study period: 2015-10-01 through 2026-11-17.

WITH daily_counts AS (
  SELECT
    DATE(block_timestamp, 'UTC') AS block_date,
    COUNT(*) AS daily_transaction_count
  FROM
    `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions`
  WHERE
    block_timestamp >= TIMESTAMP('2015-10-01 00:00:00+00')
    AND block_timestamp < TIMESTAMP('2026-11-18 00:00:00+00')
  GROUP BY
    block_date
),
calendar AS (
  SELECT
    block_date
  FROM
    UNNEST(
      GENERATE_DATE_ARRAY(DATE '2015-10-01', DATE '2026-11-17')
    ) AS block_date
)
SELECT
  calendar.block_date,
  COALESCE(daily_counts.daily_transaction_count, 0)
    AS daily_transaction_count
FROM
  calendar
LEFT JOIN
  daily_counts
USING (block_date)
ORDER BY
  calendar.block_date;
