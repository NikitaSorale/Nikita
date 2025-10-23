import seaborn as sns
import matplotlib.pyplot as plt

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Select numerical columns
numeric_data = penguins.select_dtypes(include='number')

# Compute correlation
corr = numeric_data.corr()
print(corr)

# Plot heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
