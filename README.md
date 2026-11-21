# Ethereum Network Activity Forecasting

### A Comparative Study of Statistical, Machine Learning, and Deep Learning Models (2015–2026)

## Project Overview

This project investigates the temporal characteristics and forecasting of daily transaction activity on the Ethereum blockchain.

It applies exploratory data analysis (EDA), statistical time-series methods, machine-learning algorithms, and deep-learning techniques to historical Ethereum transaction data.

The primary objective is to evaluate and compare different forecasting approaches and identify models capable of capturing temporal dependencies, recurring patterns, and changes in Ethereum network activity.

## Dataset

- **Source:** Google BigQuery Public Dataset
- **Table:** `bigquery-public-data.goog_blockchain_ethereum_mainnet.transactions`
- **Observation period:** 1 October 2015 – 17 November 2026
- **Total observations:** 4,066 daily records
- **Target variable:** Daily transaction count

The dataset was processed into a daily time series with continuous date coverage and no missing dates.

## Methodology

The project follows a chronological time-series forecasting workflow.

### 1. Exploratory Data Analysis

- Transaction-count distributions
- Long-term network activity trends
- Rolling averages and volatility
- Weekly and monthly patterns
- Monthly activity heatmaps
- Stationarity and autocorrelation analysis

### 2. Statistical Forecasting

- Naive forecasting
- Seasonal naive forecasting
- ARIMA
- SARIMA

### 3. Machine Learning

- Random Forest
- XGBoost
- Multilayer Perceptron (MLP)

### 4. Deep Learning

- Long Short-Term Memory (LSTM)

### 5. Model Evaluation

The dataset was divided chronologically into three subsets:

- **Training:** 70% (2,846 observations)
- **Validation:** 15% (610 observations)
- **Testing:** 15% (610 observations)

For the final machine-learning and deep-learning test evaluation, models were retrained using the combined training and validation data.

A rolling-origin, one-day-ahead forecasting strategy was then applied. After each prediction, the actual observation was incorporated into the historical input for the next forecast, while model parameters remained fixed.

Performance was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

## Final Test Results

The following table presents the test-set performance of the four machine-learning and deep-learning models.

| Model | MAE | RMSE | MAPE (%) |
|---|---:|---:|---:|
| LSTM | 188,525.83 | 274,566.22 | 9.38 |
| MLP | 240,435.88 | 357,392.41 | 11.51 |
| Random Forest | 341,539.07 | 491,271.85 | 15.86 |
| XGBoost | 391,641.66 | 546,286.97 | 18.23 |

**Best-performing model: LSTM**

LSTM achieved the lowest error across all three evaluation metrics.

The annual analysis also showed that all four models experienced increased prediction errors during 2026 compared with 2025. This highlights the challenges associated with changing Ethereum network activity and the limitations of models with fixed parameters.

**Evaluation note:** Fixed-origin statistical forecasts and rolling-origin machine-learning/deep-learning forecasts represent different evaluation strategies and should not be directly ranked against each other.

## Project Structure

```text
Ethereum_TimeSeries_Forecasting/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_Ethereum_TimeSeries_Forecasting.ipynb
│
├── visualizations/
│   ├── 01_transaction_count_distribution.png
│   ├── ...
│   └── 33_annual_test_performance_comparison.png
│
├── lstm_benchmark.py
├── .gitignore
└── README.md
```

*Note: Local Python virtual environments (`pytorch_env` and `pytorch312_env`) are excluded from the published project repository.*

## Technologies Used

- **Programming language:** Python
- **Development environment:** Jupyter Notebook
- **Data analysis:** pandas, NumPy
- **Data visualization:** Matplotlib
- **Statistical analysis:** statsmodels, SciPy
- **Machine learning:** scikit-learn, XGBoost
- **Deep learning:** PyTorch
- **Data source:** Google BigQuery

## Reproducibility

The primary analytical workflow is provided in:

`notebooks/01_Ethereum_TimeSeries_Forecasting.ipynb`

The processed dataset and visualization files are organized in their respective project directories.

To reproduce the analysis:

1. Configure a compatible Python environment.
2. Install the required packages.
3. Make the dataset available in the expected project location.
4. Open the Jupyter Notebook.
5. Execute the notebook cells in their intended order.

## Limitations and Future Research

Potential extensions include:

- Incorporating active addresses, gas usage, transaction fees, and smart-contract activity.
- Investigating the effects of major Ethereum network upgrades.
- Exploring hybrid statistical and deep-learning models.
- Evaluating periodic model retraining and adaptive forecasting.
- Applying explainable machine-learning methods.
- Extending the analysis to other blockchain networks.

## Conclusion

This project provides a comparative framework for analysing and forecasting daily Ethereum transaction activity using statistical, machine-learning, and deep-learning approaches.

Among the evaluated machine-learning and deep-learning models, LSTM achieved the strongest final test-set performance. However, the increased prediction errors observed during 2026 demonstrate the importance of accounting for evolving blockchain network behaviour and considering adaptive forecasting strategies in future research.