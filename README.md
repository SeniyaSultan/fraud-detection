# Fraud Detection Project – Adey Innovations Inc.

## Overview

This project focuses on detecting fraudulent transactions in both e-commerce and banking domains. Using machine learning, geolocation analysis, and transaction pattern recognition, the goal is to accurately identify fraud while minimizing false positives to preserve customer trust.

Fraud detection is challenging because false positives frustrate customers, while false negatives cause financial loss. This project emphasizes balancing these risks with data-driven insights.

---

## Project Structure

fraud-detection/
├── data/
│ ├── raw/ # Original datasets
│ └── processed/ # Cleaned and feature-engineered data
├── notebooks/
│ ├── eda_fraud_data.ipynb
│ ├── eda-creditcard.ipynb
│ ├── feature-engineering.ipynb
│ ├── data-split.ipynb
│ ├── modeling.ipynb
│ ├── shap-explainability.ipynb
│ └── README.md
├── src/
├── models/
├── scripts/
├── requirements.txt
└── README.md

---

## Datasets

1. **Fraud_Data.csv** – E-commerce transactions

   - Features: `user_id`, `signup_time`, `purchase_time`, `purchase_value`, `device_id`, `source`, `browser`, `sex`, `age`, `ip_address`
   - Target: `class` (1 = Fraud, 0 = Legitimate)

2. **IpAddress_to_Country.csv** – Maps IP ranges to countries

3. **creditcard.csv** – Bank transactions
   - Features: `Time`, `V1`–`V28` (PCA-transformed), `Amount`
   - Target: `Class` (1 = Fraud, 0 = Legitimate)

**Critical Challenge:** All datasets are highly imbalanced.

---

## Task 1 – Data Analysis & Preprocessing

- **Notebooks Completed:**

  - `eda-fraud-data.ipynb`: EDA, feature engineering, geolocation mapping
  - `eda-creditcard.ipynb`: EDA, class imbalance analysis for banking data
  - `feature-engineering.ipynb`: Timestamp transformations, transaction velocity features, scaling, encoding

- **Data Handling Highlights:**

  - Missing values addressed and duplicates removed
  - IP addresses mapped to countries to analyze fraud patterns
  - Class imbalance handled using **SMOTE** (e-commerce) and **`class_weight='balanced'`** (Random Forest)

- **Visualizations:**
  - 📌 Insert **Class Distribution** (`countplot`)
  - 📌 Insert **Purchase Value Distribution** (`histplot`)
  - 📌 Insert **Hour of Transaction by Class** (`boxplot`)
  - 📌 Insert **Top 10 Countries by Fraud Rate** (`bar chart`)

---

## Task 2 – Model Building & Evaluation

- **Models Implemented:**

  - Logistic Regression (baseline, interpretable)
  - Random Forest (ensemble, tuned: `n_estimators=200`, `max_depth=10`, `class_weight='balanced'`)

- **Evaluation Metrics:**
  - Confusion Matrix, F1-score, AUC-PR
  - Stratified K-Fold cross-validation performed
- **Class Imbalance Handling:** SMOTE / class_weight=’balanced’
- **Next Steps:** SHAP explainability (Task 3)
