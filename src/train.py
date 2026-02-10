import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from src.data_loader import load_dataset
from src.config import (
    DATA_PATH,
    TEST_SIZE,
    RANDOM_STATE,
    MODEL_PATH,
    SCALER_PATH,
)


def train():
    X, y = load_dataset(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=RANDOM_STATE,
        class_weight="balanced",
    )

    model.fit(X_train_scaled, y_train)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    return model, X_test_scaled, y_test
