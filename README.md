
🚀 Getting Started
1. Clone the Repository
git clone https://github.com/B-NANDKISHORE/SCT_ML_2.git
2. Install Dependencies
pip install -r requirements.txt
3. Run Clustering Script
python app.py

src/clustering.py

This will generate customer segments and save the visualization in plots/customer_clusters.png.

📊 Results

The dataset is clustered into 5 distinct customer groups:

Cluster 0: Low income, low spending (budget-conscious shoppers)

Cluster 1: High income, low spending (conservative spenders)

Cluster 2: Medium income, medium spending

Cluster 3: Low income, high spending (impulsive buyers)

Cluster 4: High income, high spending (premium customers)

📌 Example visualization:

🛠️ Tech Stack
Python

pandas → Data manipulation

matplotlib → Data visualization

scikit-learn → K-Means clustering

✨ Future Improvements

Include Age and Gender for richer segmentation

Apply Elbow Method and Silhouette Score for optimal cluster selection

Deploy interactive dashboard using Streamlit
