
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Product": ["Cola", "Chips", "Milk", "Juice", "Bread",
                "Cheese", "Water", "Cake", "Yogurt", "Nuts"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages",
                 "Snacks", "DAIRY", " Beverages", "snacks",
                 "dairy ", "SNACKS"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 1,800",
              "Rs. 120", "Rs. 650", "Rs. 70", "Rs. 300",
              "Rs. 220", "Rs. 500"],
    "Stock": [40, 120, 60, 30, 80, 45, 200, 75, 50, 55]
})

df["Category"] = df["Category"].str.strip().str.title()
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "").astype(float)
df["Category_Code"] = df["Category"].astype("category").cat.codes

print(df)

avg = df.groupby("Category")["Price"].mean()
stock = df.groupby("Category")["Stock"].sum()

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(avg.index, avg.values)
plt.title("Average Price")
plt.xlabel("Category")
plt.ylabel("Price")

plt.subplot(1, 2, 2)
plt.pie(stock.values, labels=stock.index, autopct="%1.1f%%")
plt.title("Stock Share")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
