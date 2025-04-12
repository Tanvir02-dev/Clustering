import pandas as pd
import os
import sys
import streamlit as st
import joblib
import seaborn as sns
import matplotlib.pyplot as plt


# Import the predict_cluster function
from src.predictor import predict_cluster

# Load the pre-trained model
model_path = os.path.join(os.path.dirname(__file__), 'src', 'model.pkl')
model = joblib.load(model_path)

# Load the dataset
data_path = os.path.join(os.path.dirname(__file__), 'data', 'mall_customers (1).csv')
data = pd.read_csv(data_path)

# Streamlit App
st.title("Mall Customers Clustering")
st.write("Dataset Preview:")
st.dataframe(data)

# Visualization: Pairplot
st.write("### Data Distribution")
fig = sns.pairplot(data[['Age', 'Annual_Income', 'Spending_Score']])
st.pyplot(fig)

# Visualization: Cluster Scatter Plot
st.write("### Clustering Visualization")
data['Cluster'] = model.predict(data[['Age', 'Annual_Income', 'Spending_Score']])
fig, ax = plt.subplots()
scatter = ax.scatter(
    data['Annual_Income'], 
    data['Spending_Score'], 
    c=data['Cluster'], 
    cmap='viridis', 
    alpha=0.7
)
ax.set_title("Clusters based on Annual Income and Spending Score")
ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score")
st.pyplot(fig)

# Input form for cluster prediction
st.write("### Predict Cluster")
age = st.number_input("Age", min_value=0, max_value=100, value=25)
income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)

if st.button("Predict"):
    # Call the predict_cluster function
    prediction = predict_cluster(model, age, income, spending_score)
    st.write(f"Predicted Cluster: {prediction}")
