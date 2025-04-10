import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# Load the dataset
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mall_customers (1).csv')
data = pd.read_csv(data_path)

# Select features for clustering
X = data[['Age', 'Annual_Income', 'Spending_Score']]

# Train the KMeans model
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# Save the model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
joblib.dump(kmeans, model_path)
print(f"Model saved to {model_path}")