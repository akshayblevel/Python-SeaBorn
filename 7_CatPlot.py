import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the data
np.random.seed(0)
data = {
    "pull_requests": np.random.randint(0, 10, size=30),
    "gender": np.random.choice(["Male", "Female"], size=30),
    "day": np.arange(1, 31)
}
df = pd.DataFrame(data)

# Add a new column to split days into weeks
df["week"] = pd.cut(df["day"], bins=[0, 7, 14, 21, 31], labels=["Week 1", "Week 2", "Week 3", "Week 4"])

# Create a catplot
sns.catplot(
    data=df,
    x="gender",
    y="pull_requests",
    col="week",         # Facet by week
    kind="swarm",       # You can also try 'box', 'violin', 'strip', etc.
    height=4,
    aspect=0.8
)

plt.suptitle("Pull Requests by Gender per Week", y=1.05)
plt.show()