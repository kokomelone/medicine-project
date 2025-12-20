import pandas as pd
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# ---------------- LOAD & CLEAN DATA ----------------

df = pd.read_csv("pharmacy.csv")

# normalize text
df["brand_name"] = df["brand_name"].str.lower()
df["primary_ingredient"] = df["primary_ingredient"].str.lower()
df["primary_strength"] = df["primary_strength"].str.lower()

# remove discontinued medicines
df = df[df["is_discontinued"] == False]

# ensure price is numeric
df["price_inr"] = pd.to_numeric(df["price_inr"], errors="coerce")

# drop rows with missing critical data
df = df.dropna(
    subset=["brand_name", "primary_ingredient", "primary_strength", "price_inr"]
)

# create salt column
df["salt"] = df["primary_ingredient"] + " " + df["primary_strength"]

# ---------------- CORE LOGIC ----------------

def find_alternatives(medicine_name):
    medicine_name = medicine_name.lower()

    # partial matching
    matches = df[df["brand_name"].str.contains(medicine_name)]

    if matches.empty:
        return None

    row = matches.iloc[0]
    salt = row["salt"]

    alternatives = df[df["salt"] == salt].sort_values(by="price_inr")

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

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search_medicine():
    medicine = request.args.get("medicine")

    if not medicine:
        return jsonify({"error": "Medicine name is required"}), 400

    result = find_alternatives(medicine)

    if not result:
        return jsonify({"error": "Medicine not found"}), 404

    return jsonify(result)


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)