from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_logistic_regression(X_train, y_train):
    print("Training Logistic Regression...")
    model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train):
    print("Training Random Forest...")
    model = RandomForestClassifier(class_weight='balanced', max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    joblib.dump(model, path)
    print(f"Model saved to {path}")
