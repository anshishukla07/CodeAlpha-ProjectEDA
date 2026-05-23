import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Dataset load ho raha hai...\n")
try:
    df = pd.read_csv("dataset.csv")
    print("✅ Dataset successfully loaded!\n")
except FileNotFoundError:
    print("❌ ERROR: 'dataset.csv.")
    exit()

# 2. Data Exploration (EDA)
print("--- 1. Data ke Pehle 5 Rows ---")
print(df.head(), "\n")

print("--- 2. Missing Values Kitni Hain? ---")
print(df.isnull().sum(), "\n")

print("--- 3. Numerical Columns Ka Summary ---")
print(df.describe(), "\n")

# 3. Graphs (Visualization)
print("⏳ DHYAN DEIN: Graph khul raha hai, use close karoge tabhi dusra khulega.\n")

# Graph 1: (Survived vs Dead)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', palette='Set1')
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()


plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], kde=True, color='purple')
plt.title("Age Distribution of Passengers")
plt.show()

print("✅ EDA project run ho gaya!")
