# BBRI Stock Price Forecast (MLOps)

End-to-end time series forecasting untuk prediksi harga penutupan saham BBRI, dari pengambilan data sampai deployment.

## Pipeline
1. **Data collection**: harga historis BBRI via `yfinance`
2. **Feature engineering**: lag price (1,2,3,5 hari) dan moving average (5,10 hari)
3. **Modeling**: Linear Regression, split kronologis (bukan acak), tracked dengan MLflow
4. **Serving**: FastAPI, di-containerize dengan Docker
5. **CI/CD**: GitHub Actions

## Hasil
Model mengalahkan baseline naif (besok = harga hari ini):
- MAE: 56.35 (vs baseline 67.88)
- R²: 0.9334 (vs baseline 0.8962)

## Cara menjalankan
```bash
docker build -t bbri-forecast-api .
docker run -p 8000:8000 bbri-forecast-api
```
Buka `http://localhost:8000/docs`

## Limitations
- Model regresi linear sederhana, belum coba model time series khusus (ARIMA, LSTM)
- Prediksi cuma 1 hari ke depan, akurasi menurun untuk horizon lebih jauh
- Tidak memperhitungkan faktor eksternal (berita, sentimen pasar, kebijakan)