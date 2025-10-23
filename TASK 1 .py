import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the 'tips' dataset
tips = sns.load_dataset("tips")

# Show first few rows (optional)
print(tips.head())

avg_bill = tips.groupby(['day', 'time'])['total_bill'].mean().reset_index()
print("Average total bill by day and time:")
print(avg_bill)

max_tip = tips.groupby('smoker')['tip'].max().reset_index()
print("\nMaximum tip amount by smoker status:")
print(max_tip)

sns.barplot(x='day', y='total_bill', hue='time', data=avg_bill)
plt.title("Average Total Bill by Day and Time")
plt.ylabel("Average Total Bill ($)")
plt.show()

sns.barplot(x='smoker', y='tip', data=max_tip)
plt.title("Maximum Tip by Smoker Status")
plt.ylabel("Maximum Tip ($)")
plt.show()
