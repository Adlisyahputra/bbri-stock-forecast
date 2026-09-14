import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from features import build_features, FEATURE_COLS

def test_build_features_output_keys():
    closes = [3100, 3110, 3105, 3120, 3130, 3125, 3135, 3140, 3150, 3160]
    features = build_features(closes)
    assert set(features.keys()) == set(FEATURE_COLS)

def test_close_lag_1_is_last_value():
    closes = [3100, 3110, 3105, 3120, 3130, 3125, 3135, 3140, 3150, 3160]
    features = build_features(closes)
    assert features['close_lag_1'] == 3160

def test_raises_error_if_too_few_data():
    try:
        build_features([100, 200, 300])
        assert False, "Harusnya raise ValueError"
    except ValueError:
        pass