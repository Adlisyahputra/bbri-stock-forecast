import pandas as pd

FEATURE_COLS = ['close_lag_1', 'close_lag_2', 'close_lag_3', 'close_lag_5', 'ma_5', 'ma_10']

def build_features(recent_closes: list) -> dict:
    """
    recent_closes: list harga penutupan berurutan dari yang PALING LAMA ke PALING BARU,
    minimal 10 hari terakhir (karena butuh ma_10).
    """
    if len(recent_closes) < 10:
        raise ValueError("Butuh minimal 10 harga penutupan terakhir")

    s = pd.Series(recent_closes)

    features = {
        'close_lag_1': s.iloc[-1],
        'close_lag_2': s.iloc[-2],
        'close_lag_3': s.iloc[-3],
        'close_lag_5': s.iloc[-5],
        'ma_5': s.iloc[-5:].mean(),
        'ma_10': s.iloc[-10:].mean(),
    }
    return features