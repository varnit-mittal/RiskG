

# RiskG - Bank of Baroda Risk Management Solution

## Overview

**RiskG** is an advanced risk management solution developed for the Bank of Baroda using Generative AI. It enhances the bank's ability to predict, assess, and mitigate various types of risks including market, credit, and operational risks.

## Objectives

The main goal of RiskG is to leverage generative AI to:
- Predict stock prices and provide actionable investment strategies.
- Monitor credit card transactions to detect anomalies and potential fraud.
- Assess loan eligibility and credit risk for better decision-making.
- Predict and manage operational risks to ensure compliance and operational efficiency.

## Key Features

### Market Risk Management
- **Stock Price Prediction Model**: Utilizes LSTM (Long Short-Term Memory) and GRU (Gated Recurrent Unit) models to forecast stock prices with high accuracy by analyzing historical and real-time market data. This helps in anticipating market trends and making informed investment decisions.
- **Generative AI for Strategic Insights**: Integrates with Azure OpenAI to provide tailored insights and investment strategies, advising on optimal investment timings and risk-adjusted returns.

### Credit Risk Management
- **Credit Card Transaction Monitoring**: Employs an AI-driven model to continuously monitor credit card transactions for anomalies, issuing real-time alerts and warnings to prevent fraud and unauthorized activities.
- **Loan Eligibility and Risk Assessment**: Evaluates customer profiles to assess creditworthiness based on comprehensive data analysis. This helps in identifying low-risk candidates for loan approvals and reducing default likelihood.

### Operational Risk Management
- **Operational Risk Prediction**: Analyzes internal processes, customer interactions, and external factors to identify potential operational risks. This ensures compliance with regulatory standards and minimizes operational disruptions.

## Business Relevance

- **Proactive Risk Mitigation**: Enables the bank to address risks before they materialize, protecting assets and maintaining customer trust.
- **Data-Driven Decision Making**: Provides AI-driven insights for making informed, strategic decisions that optimize returns and minimize exposure to risks.
- **Regulatory Compliance**: Aligns risk management practices with regulatory requirements, supporting the bank’s commitment to integrity and transparency.
- **Enhanced Customer Experience**: Improves customer satisfaction and retention by offering real-time alerts and personalized financial advice.

## Technical Details

- **Language**: Python
- **Libraries Used**: 
  - `numpy`, `pandas` for data manipulation
  - `tensorflow`, `keras` for machine learning models (LSTM, GRU)
  - `scikit-learn` for additional ML algorithms
  - `azure-openai` for integrating with Azure OpenAI

## Examples

1. **Stock Price Prediction**:
   ```python
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import LSTM, Dense
   # Define and compile your LSTM model here
   ```

2. **Credit Card Transaction Monitoring**:
   ```python
   from sklearn.ensemble import IsolationForest
   # Use Isolation Forest for anomaly detection in transaction data
   ```

3. **Loan Eligibility Assessment**:
   ```python
   from sklearn.linear_model import LogisticRegression
   # Train a Logistic Regression model for creditworthiness evaluation
   ```

4. **Operational Risk Prediction**:
   ```python
   from sklearn.ensemble import RandomForestClassifier
   # Implement RandomForestClassifier for predicting operational risks
   ```

## Installation

To set up and run RiskG, clone this repository and install the required dependencies:

```bash
git clone https://github.com/your-repo/riskg.git
cd riskg
pip install -r requirements.txt
```

