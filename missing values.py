import pandas as pd

# === CONFIG ===
file_path = "\\KIT B1 - AP.csv"

# === LOAD DATA ===
df = pd.read_csv(file_path,encoding="latin-1")

# === CALCULATE MISSING VALUES ===
missing_count = df.isna().sum()
missing_percent = (missing_count / len(df)) * 100

# === COMBINE INTO ONE TABLE ===
missing_table = pd.DataFrame({
    "missing_values": missing_count,
    "missing_percent": missing_percent
}).sort_values(by="missing_percent", ascending=False)

print(missing_table)