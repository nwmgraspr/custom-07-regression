"""
app_tips_case.py

Author: Ralph Massaquoi
Date: 2026-06


Purpose:
    - investigate whether restaurant bill size predicts tip amount
    - perform simple linear regression using scikit-learn
    - evaluate model fit with residuals, R-squared, and RMSE
    - visualize the fitted regression line
    - analyze residual patterns
    - predict tip amount for a selected bill value

Data Source:
    Seaborn Tips Dataset

Business Question:
    Can the total bill amount be used to predict the tip left by customers?

Run:

uv run python -m datafun.app_tips_case
"""

# === Section 1a. Imports ===

import logging
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

# === Section 1b. Configure Logger ===

LOG: logging.Logger = get_logger("P07", level="DEBUG")
log_header(LOG, "P07")

# === Section 1c. Global Constants ===

DATASET_NAME: Final[str] = "tips"

FEATURE_COL: Final[str] = "total_bill"
TARGET_COL: Final[str] = "tip"

FEATURE_LABEL: Final[str] = "Total Bill ($)"
TARGET_LABEL: Final[str] = "Tip Amount ($)"

EXAMPLE_FEATURE_VALUE: Final[float] = 50.0

# === Section 1d. Pandas Display Settings ===

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)

# === Section 2. Load Data ===


def load_data() -> pd.DataFrame:
    """Load the Tips dataset."""
    LOG.info(f"Loading dataset: {DATASET_NAME}")

    df: pd.DataFrame = sns.load_dataset(DATASET_NAME)

    LOG.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")

    LOG.info("First Five Rows")
    LOG.info(f"\n{df.head()}")

    LOG.info("Summary Statistics")
    LOG.info(f"\n{df[[FEATURE_COL, TARGET_COL]].describe()}")

    correlation: float = df[FEATURE_COL].corr(df[TARGET_COL])
    LOG.info(f"Correlation between {FEATURE_COL} and {TARGET_COL}: {correlation:.4f}")

    return df


# === Section 3. Prepare Modeling Data ===


def make_model_view(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing feature or target values."""

    LOG.info("Creating modeling view")

    cols_required = [FEATURE_COL, TARGET_COL]

    df_model: pd.DataFrame = df.dropna(subset=cols_required).copy()

    LOG.info(f"Original rows: {df.shape[0]}")
    LOG.info(f"Model rows: {df_model.shape[0]}")
    LOG.info(f"Rows dropped: {df.shape[0] - df_model.shape[0]}")

    return df_model


# === Section 4. Build X and y ===


def build_x_and_y(df_model: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Build feature matrix and target vector."""

    X: np.ndarray = df_model[[FEATURE_COL]].to_numpy()
    y: np.ndarray = df_model[TARGET_COL].to_numpy()

    LOG.debug(f"X shape: {X.shape}")
    LOG.debug(f"y shape: {y.shape}")

    return X, y


# === Section 5. Fit Model ===


def fit_line(X: np.ndarray, y: np.ndarray) -> LinearRegression:
    """Fit linear regression model."""

    LOG.info("Fitting linear regression model")

    model = LinearRegression()
    model.fit(X, y)

    slope: float = float(model.coef_[0])
    intercept: float = float(model.intercept_)

    LOG.info("Regression Equation:")
    LOG.info(f"{TARGET_COL} = {slope:.6f} * {FEATURE_COL} + {intercept:.6f}")

    return model


# === Section 6. Predict ===


def predict(model: LinearRegression, X: np.ndarray) -> np.ndarray:
    """Generate fitted values and example prediction."""

    y_hat: np.ndarray = model.predict(X)

    X_example = np.array([[EXAMPLE_FEATURE_VALUE]])

    prediction: float = float(model.predict(X_example)[0])

    LOG.info(
        f"Predicted tip for a bill of ${EXAMPLE_FEATURE_VALUE:.2f}: ${prediction:.2f}"
    )

    return y_hat


# === Section 7. Evaluate Fit ===


def examine_fit(
    model: LinearRegression,
    X: np.ndarray,
    y: np.ndarray,
    y_hat: np.ndarray,
) -> np.ndarray:
    """Calculate residuals, R-squared, and RMSE."""

    residuals: np.ndarray = y - y_hat

    r_squared: float = model.score(X, y)

    rmse: float = float(np.sqrt(np.mean(residuals**2)))

    LOG.info("====================")
    LOG.info("MODEL EVALUATION")
    LOG.info("====================")

    LOG.info(f"R-squared: {r_squared:.4f}")
    LOG.info(f"RMSE: {rmse:.4f}")

    LOG.info(f"Residual Min: {np.min(residuals):.4f}")
    LOG.info(f"Residual Max: {np.max(residuals):.4f}")
    LOG.info(f"Residual Mean: {np.mean(residuals):.4f}")

    return residuals


# === Section 8. Create Visualizations ===


def make_plots(
    df_model: pd.DataFrame,
    y_hat: np.ndarray,
    residuals: np.ndarray,
) -> None:
    """Create regression and residual plots."""

    feature_values = df_model[FEATURE_COL].to_numpy()
    target_values = df_model[TARGET_COL].to_numpy()

    plt.figure(figsize=(10, 6))

    scatter_plt: Axes = sns.scatterplot(
        x=feature_values,
        y=target_values,
    )

    order = np.argsort(feature_values)

    scatter_plt.plot(
        feature_values[order],
        y_hat[order],
        color="red",
        linewidth=2,
    )

    scatter_plt.set_xlabel(FEATURE_LABEL)
    scatter_plt.set_ylabel(TARGET_LABEL)
    scatter_plt.set_title("Total Bill vs Tip Amount with Regression Line")

    plt.figure(figsize=(10, 6))

    residual_plt: Axes = sns.scatterplot(
        x=feature_values,
        y=residuals,
    )

    residual_plt.axhline(
        y=0,
        color="red",
        linestyle="--",
    )

    residual_plt.set_xlabel(FEATURE_LABEL)
    residual_plt.set_ylabel("Residuals")
    residual_plt.set_title("Residual Plot")


# === Section 9. Summary ===


def summarize(
    df: pd.DataFrame,
    df_model: pd.DataFrame,
    model: LinearRegression,
) -> None:
    """Display summary information."""

    slope = float(model.coef_[0])
    intercept = float(model.intercept_)

    LOG.info("====================")
    LOG.info("SUMMARY")
    LOG.info("====================")

    LOG.info(f"Dataset: {DATASET_NAME}")
    LOG.info(f"Feature: {FEATURE_COL}")
    LOG.info(f"Target: {TARGET_COL}")

    LOG.info(f"Original Rows: {df.shape[0]}")
    LOG.info(f"Model Rows: {df_model.shape[0]}")

    LOG.info(
        f"Regression Equation: "
        f"{TARGET_COL} = {slope:.6f} * "
        f"{FEATURE_COL} + {intercept:.6f}"
    )

    LOG.info(
        "Interpret the R-squared, RMSE, and residual plots "
        "to determine whether a linear model is appropriate."
    )


# === Main Function ===


def main() -> None:

    log_header(LOG, "REGRESSION")

    LOG.info("Starting regression workflow")

    df = load_data()

    df_model = make_model_view(df)

    X, y = build_x_and_y(df_model)

    model = fit_line(X, y)

    y_hat = predict(model, X)

    residuals = examine_fit(model, X, y, y_hat)

    make_plots(df_model, y_hat, residuals)

    summarize(df, df_model, model)

    plt.show()

    LOG.info("Regression workflow complete")

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === Execution Guard ===

if __name__ == "__main__":
    main()
