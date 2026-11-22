# Ethereum Network Activity Forecasting

### A Comparative Study of Statistical, Machine Learning, and Deep Learning Models (2015–2026)

## Project Overview

This project investigates the temporal characteristics and forecasting of daily transaction activity on the Ethereum blockchain. It applies exploratory data analysis, statistical time-series methods, machine-learning algorithms, and deep-learning techniques to historical Ethereum transaction data.

## Dataset

- **Source:** Google BigQuery Public Dataset (Google Cloud Blockchain Analytics)
- **Table:** `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions`
- **Observation period:** 1 October 2015 – 17 November 2026
- **Total observations:** 4,066 daily records
- **Target variable:** Daily transaction count
- **Date convention in the documented SQL:** UTC calendar days

The processed daily series has continuous calendar coverage. See [the SQL documentation](sql/README.md) and [the extraction query](sql/daily_transaction_counts.sql) for the documented aggregation logic and provenance notes.

## Methodology

The project follows a chronological time-series forecasting workflow.

### Exploratory data analysis

- Transaction-count distributions and long-term trends
- Rolling averages and volatility
- Weekly and monthly patterns
- Stationarity and autocorrelation analysis

### Forecasting models

- Benchmarks: naïve and seasonal naïve
- Statistical: ARIMA and SARIMA
- Machine learning: Random Forest, XGBoost, and multilayer perceptron (MLP)
- Deep learning: long short-term memory (LSTM)

### Model evaluation

The dataset was divided chronologically:

- **Training:** 2,846 observations (70%; 1 Oct 2015 – 16 Jul 2023)
- **Validation:** 610 observations (15%; 17 Jul 2023 – 17 Mar 2025)
- **Testing:** 610 observations (15%; 18 Mar 2025 – 17 Nov 2026)

For the final machine-learning and deep-learning test evaluation, models were retrained using the combined training and validation history. A rolling-origin, one-day-ahead forecasting strategy was then applied. After each prediction, the actual observation was incorporated into the history for the next forecast, while model parameters remained fixed.

Performance was evaluated using MAE, RMSE, and MAPE. Fixed-origin statistical forecasts and rolling-origin forecasts represent different evaluation strategies and should not be directly ranked against each other.

## Final test results

The following table presents the final 610-observation test-set performance of the four machine-learning and deep-learning models.

| Model | MAE | RMSE | MAPE (%) |
|---|---:|---:|---:|
| LSTM | 188,525.83 | 274,566.22 | 9.38 |
| MLP | 240,435.88 | 357,392.41 | 11.51 |
| Random Forest | 341,539.07 | 491,271.85 | 15.86 |
| XGBoost | 391,641.66 | 546,286.97 | 18.23 |

Among these four models in this final test experiment, LSTM achieved the lowest error on all three reported measures. Statistical models were not evaluated in this same final test experiment, so this table does not establish a winner across every model family considered.

## Project structure

```text
Ethereum_TimeSeries_Forecasting/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_Ethereum_TimeSeries_Forecasting.ipynb
├── sql/
│   ├── daily_transaction_counts.sql
│   └── README.md
├── visualizations/
│   └── [numbered analysis figures]
├── lstm_benchmark.py
└── README.md
```

Local Python virtual environments are excluded from the published repository.

## Reproducibility

The main analysis is in `notebooks/01_Ethereum_TimeSeries_Forecasting.ipynb`.

### Data extraction

1. Read [sql/README.md](sql/README.md) before running the query.
2. Run [sql/daily_transaction_counts.sql](sql/daily_transaction_counts.sql) in BigQuery Standard SQL.
3. Export the result to CSV and preserve the unmodified export.
4. Verify that it contains 4,066 daily rows from 2015-10-01 through 2026-11-17.
5. Record the extraction date, query commit, output filename, and (ideally) a SHA-256 checksum for the exported CSV.

**Query provenance:** The SQL file currently in the repository is a documented reconstruction of the daily aggregation. It is not claimed to be the exact original query that generated the historical processed CSV, because the original query text was not available in the project history. For exact replication of the original dataset, the original SQL and original export must be archived and checked against one another.

### Analysis

1. Configure a compatible Python environment and install the required packages.
2. Place the verified processed dataset at the location expected by the notebook, or update the notebook's data path.
3. Open the notebook and execute its cells in order.
4. Retain the notebook, figures, environment/package versions, and model configuration with the project revision.

## Technologies

Python, Jupyter Notebook, pandas, NumPy, Matplotlib, statsmodels, SciPy, scikit-learn, XGBoost, PyTorch, and Google BigQuery.

## Limitations and future research

Potential extensions include adding active addresses, gas usage, transaction fees, and smart-contract activity; investigating possible effects of network upgrades; testing hybrid models; evaluating periodic model retraining; and applying explainable machine-learning methods.

## Conclusion

This project provides a comparative framework for analysing and forecasting daily Ethereum transaction activity. LSTM achieved the strongest final test performance among the four machine-learning and deep-learning models evaluated in that test experiment. The increase in errors during the 2026 test segment highlights the importance of evaluating models across changing periods and considering adaptive forecasting strategies.

## Research Reports

The full research report presents the methodology, exploratory data analysis, forecasting models, validation strategy, results, and conclusions of this Ethereum network activity forecasting project.

### Available Formats

- [PDF Report](reports/Ethereum_Network_Activity_Forecasting_Report.pdf)
- [Word Report](reports/Ethereum_Network_Activity_Forecasting_Report.docx)
- [Markdown Report](reports/Ethereum_Network_Activity_Forecasting_Report.md)

The Markdown report includes all 33 figures, stored in `reports/Ethereum_Forecasting_Markdown_Assets/`.

**[Read the Research Report](reports/Ethereum_Network_Activity_Forecasting_Report.docx)**
