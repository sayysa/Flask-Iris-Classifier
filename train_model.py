from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Define paths
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'iris_classifier.joblib')

def train_model():
    # Load iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Train a machine learning model (Random Forest for example)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model using joblib
    joblib.dump(model, model_path)
    print(f"Model trained and saved at: {model_path}")

if __name__ == "__main__":
    train_model()
