from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Load the Iris dataset
iris = load_iris()
X_train = pd.DataFrame(iris.data, columns=iris.feature_names)
y_train = iris.target

# Train a Random Forest classifier on the Iris dataset
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Save the trained model to a file
model_filename = 'iris_rf_model.pkl'
joblib.dump(model, model_filename)
