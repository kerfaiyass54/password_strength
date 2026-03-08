import pandas as pd
from src.config import (
    PASSWORD_COLUMN,
    TARGET_COLUMN,
    MIN_STRENGTH,
    MAX_STRENGTH,
)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    # Keep only first two columns if extra columns exist
    df = df.iloc[:, :2]

    # Rename columns to expected names
    df.columns = [PASSWORD_COLUMN, TARGET_COLUMN]


    # Drop rows where password or strength is missing
    df = df.dropna(subset=[PASSWORD_COLUMN, TARGET_COLUMN])

    # Ensure password is string
    df[PASSWORD_COLUMN] = df[PASSWORD_COLUMN].astype(str)

    # Remove empty passwords
    df = df[df[PASSWORD_COLUMN].str.strip().str.len() > 0]

    # Keep only valid strength range
    df = df[df[TARGET_COLUMN].between(MIN_STRENGTH, MAX_STRENGTH)]

    # Remove duplicate passwords
    df = df.drop_duplicates(subset=[PASSWORD_COLUMN])

    # Reset index
    df = df.reset_index(drop=True)

    return df