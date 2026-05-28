from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from imblearn.over_sampling import SMOTE


def split_data(X, y):
    """
    Split data into train and test sets.
    """

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def scale_data(X_train, X_test):
    """
    Scale numerical variables.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled


def apply_smote(X_train, y_train):
    """
    Balance classes using SMOTE.
    """

    smote = SMOTE(random_state=42)

    X_train_smote, y_train_smote = smote.fit_resample(
        X_train,
        y_train
    )

    return X_train_smote, y_train_smote


def train_model(X_train, y_train):
    """
    Train Logistic Regression model.
    """

    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(X_train, y_train)

    return model