import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# Sample data
data = {
    "pull_requests": np.random.randint(0, 10, size=30),
    "gender": np.random.choice(["Male", "Female"], size=30),
    "day": np.arange(1, 31)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot histogram of pull_requests
sns.histplot(data=df, x="pull_requests", bins=10, kde=True)
plt.title("Histogram of Total Pull Requests")
plt.xlabel("Total Pull Requests")
plt.ylabel("Count")
plt.show()

sns.histplot(data=df, x="pull_requests", hue="gender", bins=10, kde=True, palette="pastel", multiple="stack")
plt.title("Total pull_requests by gender")
plt.xlabel("Total Pull Requests")
plt.ylabel("Count")
plt.show()