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

# Create violin plot
sns.violinplot(data=df, x="gender", y="pull_requests", palette="Set2")

# Add title and labels
plt.title("Violin Plot: Pull Requests by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Pull Requests")
plt.show()