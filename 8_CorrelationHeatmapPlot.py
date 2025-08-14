import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame with numeric columns
np.random.seed(0)
data = {
    "pull_requests": np.random.randint(0, 10, size=30),
    "day": np.arange(1, 31),
    "activity_score": np.random.normal(50, 10, size=30)
}
df = pd.DataFrame(data)

# Compute correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()