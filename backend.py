import pandas as pd

print("Script started")

df = pd.read_csv("pharmacy.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.columns)
# ---------- DATA CLEANING ----------

# lowercase text fields
df["brand_name"] = df["brand_name"].str.lower()
df["primary_ingredient"] = df["primary_ingredient"].str.lower()
df["primary_strength"] = df["primary_strength"].str.lower()

# remove discontinued medicines
df = df[df["is_discontinued"] == False]

# ensure price is numeric
df["price_inr"] = pd.to_numeric(df["price_inr"], errors="coerce")

# drop rows with missing critical data
df = df.dropna(subset=["brand_name", "primary_ingredient", "primary_strength", "price_inr"])

print("Cleaned dataset size:", df.shape)
# ---------- SALT CREATION ----------

df["salt"] = df["primary_ingredient"] + " " + df["primary_strength"]

print("Sample salt values:")
print(df["salt"].head())
# ---------- CORE LOGIC ----------

def find_alternatives(medicine_name):
    medicine_name = medicine_name.lower()

    matches = df[df["brand_name"].str.contains(medicine_name)]

    if matches.empty:
        return None

    row = matches.iloc[0]
    salt = row["salt"]

    alternatives = df[df["salt"] == salt]

    # sort by price
    alternatives = alternatives.sort_values(by="price_inr")

    # cheapest & costliest
    cheapest = alternatives.iloc[0]
    costliest = alternatives.iloc[-1]

    return {
        "searched_medicine": medicine_name,
        "salt_composition": salt,
        "total_alternatives": int(len(alternatives)),
        "price_range": {
            "min": float(round(alternatives["price_inr"].min(), 2)),
            "max": float(round(alternatives["price_inr"].max(), 2)),
            "average": float(round(alternatives["price_inr"].mean(), 2))
        },
        "best_budget_option": {
            "name": cheapest["brand_name"],
            "price": float(cheapest["price_inr"]),
            "manufacturer": cheapest["manufacturer"]
        },
        "most_expensive_option": {
            "name": costliest["brand_name"],
            "price": float(costliest["price_inr"]),
            "manufacturer": costliest["manufacturer"]
        },
        "alternatives": alternatives[
            ["brand_name", "price_inr", "manufacturer"]
        ].head(10).to_dict("records")
    }
result = find_alternatives("allegra 120mg tablet")
print(result)