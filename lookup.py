import pandas as pd

df = pd.read_json("physics_quantities.json")

query = input("Quantity: ")
result = df[df["Name"].str.lower() == query.lower()]

if not result.empty:
    print(result.to_dict(orient="records")[0])
else:
    print("Quantity not found")
