import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "pull_requests": np.random.randint(0, 10, size=30),
    "gender": np.random.choice(["Male", "Female"], size=30),
    "day": np.arange(1, 31)
}

df = pd.DataFrame(data)

# Create a displot (histogram) of pull_requests grouped by gender
sns.displot(
    data=df,
    x="pull_requests",
    hue="gender",
    bins=10,
    multiple="dodge",      # or "stack", "fill", "layer"
    kde=True,
    palette="Set1"
)

plt.title("Distribution of Pull Requests by Gender")
plt.xlabel("Number of Pull Requests")
plt.ylabel("Count")
plt.show()