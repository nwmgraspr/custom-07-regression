# Restaurant Tips Regression Analysis

# Author:
-Ralph Massaquoi
 Date: June 2026

## Overview

This project examines whether a restaurant customer's total bill can be used to predict the tip they leave. Using the Seaborn Tips dataset, a simple linear regression model is built with scikit-learn and evaluated through statistical metrics and visualizations.

## Business Question

**Can the total bill amount predict the tip left by customers?**

Understanding this relationship helps evaluate whether bill size alone is a useful predictor of tipping behavior.

## Dataset

**Source:** Seaborn Tips Dataset

## Methodology

The workflow includes:

1. Loading and exploring the dataset
2. Cleaning data and removing missing values
3. Building feature and target variables
4. Training a simple linear regression model
5. Generating predictions
6. Evaluating model performance

## Evaluation Metrics

The model is assessed using:

* **Correlation** between bill amount and tip amount
* **R-squared** to measure explained variation
* **RMSE** to measure prediction error
* **Residual analysis** to evaluate model assumptions

## Visualizations

The project creates:

* A scatterplot with a fitted regression line
* A residual plot for diagnostic analysis

## Technologies

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Scikit-learn

## Running the Project

```bash
uv run python -m datafun.app_tips_case
```

## Outputs

The program produces:

* Dataset summary statistics
* Regression equation
* Example tip prediction
* R-squared and RMSE values
* Residual statistics
* Regression and residual plots

## Conclusion

This project demonstrates how simple linear regression can be used to investigate the relationship between restaurant bill totals and tipping behavior. The results help determine whether total bill amount is a meaningful predictor of customer tips.
