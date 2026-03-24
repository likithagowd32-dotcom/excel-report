import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
data = pd.read_csv("data.csv")

# Step 2: Create pivot table (total per category)
pivot = data.pivot_table(values="Amount", index="Category", aggfunc="sum")

# Step 3: Create chart
pivot.plot(kind="bar", legend=False)
plt.title("Expense by Category")
plt.ylabel("Amount")
plt.savefig("chart.png")
plt.close()

# Step 4: Save to Excel
with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    data.to_excel(writer, sheet_name="Raw Data", index=False)
    pivot.to_excel(writer, sheet_name="Summary")

print("Excel report created successfully!")