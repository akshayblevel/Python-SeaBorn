import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the custom data
data = {
    "pull_requests": np.random.randint(0, 10, size=30),
    "gender": np.random.choice(["Male", "Female"], size=30),
    "day": np.arange(1, 31)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Stripplot
plt.figure(figsize=(8, 5))
sns.stripplot(x="gender", y="pull_requests", data=df, jitter=True)
plt.title("Stripplot of Pull Requests by Gender")
plt.show()

# Swarmplot
plt.figure(figsize=(8, 5))
sns.swarmplot(x="gender", y="pull_requests", data=df)
plt.title("Swarmplot of Pull Requests by Gender")
plt.show()

'''
x="gender": Categorical variable used to group data.
y="pull_requests": Numeric variable being plotted.
jitter=True (for stripplot): Helps spread out overlapping dots.
Swarmplot automatically avoids overlap.
'''