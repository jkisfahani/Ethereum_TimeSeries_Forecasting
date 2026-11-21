# References and citation guide

This file provides bibliographic references and suggested in-text citation locations for the standalone research report:

**Ethereum Network Activity Forecasting: A Comparative Study of Statistical, Machine Learning, and Deep Learning Models (2015–2026)**

## Suggested in-text citation placement

| Report section | Topic | Suggested citation |
|---|---|---|
| 2.1 Data source | Google BigQuery Blockchain Analytics dataset and Ethereum transaction table | (Google Cloud, n.d.-a, n.d.-b) |
| 3 Data acquisition | BigQuery SQL-based access and daily transaction aggregation | (Google Cloud, n.d.-b) |
| 4.1 Forecasting design | Time-series forecasting, chronological evaluation, rolling-origin assessment | (Hyndman & Athanasopoulos, 2021) |
| 4.2 Stationarity testing | Augmented Dickey–Fuller and KPSS tests | (Dickey & Fuller, 1979; Kwiatkowski et al., 1992) |
| 4.3 ARIMA/SARIMA | ARIMA-family modelling | (Box et al., 2015; Hyndman & Athanasopoulos, 2021) |
| 4.4 Random Forest | Random Forest regression | (Breiman, 2001) |
| 4.5 XGBoost | Gradient-boosted tree modelling | (Chen & Guestrin, 2016) |
| 4.6 MLP | Multilayer perceptron and back-propagation | (Rumelhart et al., 1986) |
| 4.7 LSTM | Long short-term memory networks | (Hochreiter & Schmidhuber, 1997) |
| 4.8 Evaluation metrics | Forecast accuracy measures, including MAE, RMSE, and MAPE | (Hyndman & Koehler, 2006) |

Use citations only where the cited source supports the specific methodological statement. The table is a placement guide, not a claim that every method was implemented exactly as described in the cited source.

## References (APA 7th edition)

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: Forecasting and control* (5th ed.). Wiley.

Breiman, L. (2001). Random forests. *Machine Learning, 45*, 5–32. https://doi.org/10.1023/A:1010933404324

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785–794). Association for Computing Machinery. https://doi.org/10.1145/2939672.2939785

Dickey, D. A., & Fuller, W. A. (1979). Distribution of the estimators for autoregressive time series with a unit root. *Journal of the American Statistical Association, 74*(366a), 427–431. https://doi.org/10.1080/01621459.1979.10482531

Google Cloud. (n.d.-a). *Blockchain Analytics Ethereum dataset*. https://docs.cloud.google.com/blockchain-analytics/docs/dataset-ethereum

Google Cloud. (n.d.-b). *Ethereum Mainnet example queries*. https://docs.cloud.google.com/blockchain-analytics/docs/example-ethereum

Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation, 9*(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735

Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3rd ed.). OTexts. https://otexts.com/fpp3/

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting, 22*(4), 679–688. https://doi.org/10.1016/j.ijforecast.2006.03.001

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. *Journal of Econometrics, 54*(1–3), 159–178. https://doi.org/10.1016/0304-4076(92)90104-Y

Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature, 323*, 533–536. https://doi.org/10.1038/323533a0

## Dataset provenance note

The notebook imports the processed CSV file and does not preserve the original BigQuery SQL statement. The SQL script at `sql/daily_transaction_counts.sql` is therefore a reproducible reconstruction based on the official Google Cloud Ethereum Mainnet transaction table and the study's documented date range. It should be compared with the archived CSV before being described as the exact query that generated the original dataset.
