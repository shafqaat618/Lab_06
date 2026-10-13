
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create messy student data
names = [" ali", "SARA ", "bilal", " Ayesha",
         "HAMZA", "zain ", "Noor", " usman "]

marks = ["72", "85", "absent", "64",
         "90", "78", "81", "69"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Step 2: Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# Step 3: Convert marks into numbers
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Step 4: Replace missing marks with mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# Step 5: Print cleaned data
print("Cleaned Student Marks:")
print(df)

# Step 6: Create bar chart
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue")

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()

# Step 7: Save and show chart
plt.savefig("marks_bar.png")
plt.show()

print("Saved marks_bar.png")
