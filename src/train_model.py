import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from xgboost import XGBClassifier  # Import XGBoost

# Add the src folder to the system path
sys.path.append("c:/Users/sadhs/Desktop/botnet detection system/src")

# Import the preprocessing function
from preprocess import load_and_preprocess_data

def train_and_evaluate_model(attack_file,normal_file):
    # Load and preprocess data
    data = load_and_preprocess_data(attack_file,normal_file)

    # Define features and labels
    X = data.drop('Label', axis=1)  # Replace 'Label' with your target column
    y = data['Label']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the Random Forest model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    print("Random Forest model training completed.")

    # Evaluate the Random Forest model
    rf_y_pred = rf_model.predict(X_test)
    print("Random Forest Accuracy:", accuracy_score(y_test, rf_y_pred))
    print("Random Forest Classification Report:")
    print(classification_report(y_test, rf_y_pred))

    # Visualize feature importance for Random Forest
    rf_feature_importances = rf_model.feature_importances_
    plt.figure(figsize=(10, 6))
    sns.barplot(x=rf_feature_importances, y=X.columns)
    plt.title("Random Forest Feature Importance")
    plt.show()

    # Save the Random Forest model
    joblib.dump(rf_model, "Results/random_forest_model.pkl")
    print("Random Forest model saved to 'Results/random_forest_model.pkl'.")

    # Train the XGBoost model
    xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    xgb_model.fit(X_train, y_train)
    print("XGBoost model training completed.")

    # Evaluate the XGBoost model
    xgb_y_pred = xgb_model.predict(X_test)
    print("XGBoost Accuracy:", accuracy_score(y_test, xgb_y_pred))
    print("XGBoost Classification Report:")
    print(classification_report(y_test, xgb_y_pred))

    # Visualize feature importance for XGBoost
    xgb_feature_importances = xgb_model.feature_importances_
    plt.figure(figsize=(10, 6))
    sns.barplot(x=xgb_feature_importances, y=X.columns)
    plt.title("XGBoost Feature Importance")
    plt.show()

    # Save the XGBoost model
    joblib.dump(xgb_model, "Results/xgboost_model.pkl")
    print("XGBoost model saved to 'Results/xgboost_model.pkl'.")

if __name__ == "__main__":
    attack_file = "data/CTU13_Attack_Traffic.csv"
    normal_file = "data/CTU13_Normal_Traffic.csv"
    train_and_evaluate_model(attack_file,normal_file)
