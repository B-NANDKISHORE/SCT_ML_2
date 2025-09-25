import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
customers = pd.read_csv("Mall_Customers.csv")

# Select features for clustering
X = customers[["Annual Income (k$)", "Spending Score (1-100)"]]

# Apply KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
y_kmeans = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# Plot clusters
plt.figure(figsize=(10, 7))
plt.scatter(X["Annual Income (k$)"], X["Spending Score (1-100)"], c=y_kmeans, cmap='viridis', s=70)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=250, marker='X', label='Centroids')
plt.title("Customer Segments using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.grid(True)
plt.show()
