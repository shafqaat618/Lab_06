
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": pd.date_range("2026-04-01", periods=15).astype(str),
    "City": [" lahore", "LAHORE ", "Lahore"] * 5,
    "Temperature": ["32C", "30C", "33C", "28C", "35C",
                    "31C", "34C", "27C", "29C", "36C",
                    "30C", "37C", "26C", "31C", "35C"],
    "Humidity": [45, None, 42, 78, 40, 60, None, 82,
                 65, 38, 62, None, 85, 58, 44],
    "Condition": ["sunny", " CLOUDY", "Sunny ", " Rainy",
                  "SUNNY", "cloudy ", "Sunny", " Rainy",
                  "CLOUDY ", "sunny", "Cloudy", "sunny ",
                  "RAINY", "Cloudy ", "sunny"]
})

# Add duplicate row
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

# Clean data
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "").astype(float)
df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates()
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].median())

print("Rows:", len(df))
print("Median:", df["Humidity"].median())
print("Correlation:", df["Temperature"].corr(df["Humidity"]))

encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print(encoded.filter(like="Condition_").head())

counts = df["Condition"].value_counts()
print(counts)

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].plot(df["Date"], df["Temperature"], marker="o")
ax[0, 0].set_title("Temperature Over Time")
ax[0, 0].set_xlabel("Date")
ax[0, 0].set_ylabel("Temperature")
ax[0, 0].tick_params(axis="x", rotation=45)

ax[0, 1].scatter(df["Temperature"], df["Humidity"])
ax[0, 1].set_title("Temperature vs Humidity")
ax[0, 1].set_xlabel("Temperature")
ax[0, 1].set_ylabel("Humidity")

ax[1, 0].pie(counts.values, labels=counts.index, autopct="%1.1f%%")
ax[1, 0].set_title("Weather Conditions")

ax[1, 1].hist(df["Temperature"], bins=5)
ax[1, 1].set_title("Temperature Distribution")
ax[1, 1].set_xlabel("Temperature")
ax[1, 1].set_ylabel("Days")

fig.suptitle("Weather Overview")
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
