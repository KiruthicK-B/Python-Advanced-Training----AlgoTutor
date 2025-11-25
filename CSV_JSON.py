import pandas as pd

df = pd.read_csv("Food_Delivery_Route_Efficiency_Dataset.csv")


df.to_json("Food_Delivery_Route_Efficiency_Dataset.json", orient="records", indent=4)

print("CSV successfully converted to JSON!")
