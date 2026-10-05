import pandas as pd

def solution(df):
    df = df.copy()

# Step 1: Drop columns with more than 50% missing values
    keep_cols = []

    for col in df.columns:
        if df[col].isna().mean() <= 0.5:
            keep_cols.append(col)

    df = df[keep_cols]

# Step 2: Drop rows with more than 50% missing values
    df = df[df.isna().mean(axis=1) <= 0.5]

# Step 3: Fill remaining missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Step 4: Reset index
    df = df.reset_index(drop=True)

    return df