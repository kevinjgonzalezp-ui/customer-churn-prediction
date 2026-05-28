import pandas as pd


def clean_data(df):
    """
    Clean the customer churn dataset.
    """
    df = df.copy()

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()
    df = df.drop("customerID", axis=1)

    return df


def encode_data(df):
    """
    Encode categorical variables for Machine Learning models.
    """
    df = df.copy()

    binary_columns = ["Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]

    for col in binary_columns:
        df[col] = df[col].map({"Yes": 1, "No": 0})

    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    categorical_cols = [
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaymentMethod"
    ]

    df_encoded = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    return df_encoded