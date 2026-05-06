import pandas as pd
import matplotlib.pyplot as plt
import os

filename = "smart_restaurant_pricing_sensor_based.csv"
df = pd.read_csv(filename)


plt.figure(figsize=(8, 5))
plt.scatter(df["Demand_Index"], df["Recommended_Price_EUR"])
plt.xlabel("Demand Index")
plt.ylabel("Recommended Price (EUR)")
plt.title("Demand Index vs Recommended Price")
plt.grid(True)
plt.savefig("graph_1_demand_vs_price.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Stock_Level"], df["Recommended_Price_EUR"])
plt.xlabel("Stock Level (%)")
plt.ylabel("Recommended Price (EUR)")
plt.title("Stock Level vs Recommended Price")
plt.grid(True)
plt.savefig("graph_2_stock_vs_price.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Pricing_Score"], df["Price_Adjustment_Percentage"])
plt.xlabel("Pricing Score")
plt.ylabel("Price Adjustment (%)")
plt.title("Pricing Score vs Price Adjustment")
plt.grid(True)
plt.savefig("graph_3_score_vs_adjustment.png", dpi=300, bbox_inches="tight")
plt.show()


decision_counts = df["Decision"].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(decision_counts.index, decision_counts.values)
plt.xlabel("Pricing Decision")
plt.ylabel("Number of Scenarios")
plt.title("Distribution of Pricing Decisions")
plt.grid(axis="y")
plt.savefig("graph_4_decision_distribution.png", dpi=300, bbox_inches="tight")
plt.show()


avg_adjustment = df.groupby("Product_Name")["Price_Adjustment_Percentage"].mean().sort_values()

plt.figure(figsize=(10, 5))
plt.bar(avg_adjustment.index, avg_adjustment.values)
plt.xlabel("Product")
plt.ylabel("Average Price Adjustment (%)")
plt.title("Average Price Adjustment by Product")
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y")
plt.savefig("graph_5_avg_adjustment_by_product.png", dpi=300, bbox_inches="tight")
plt.show()


avg_price = df.groupby("Product_Name")["Recommended_Price_EUR"].mean().sort_values()

plt.figure(figsize=(10, 5))
plt.bar(avg_price.index, avg_price.values)
plt.xlabel("Product")
plt.ylabel("Average Recommended Price (EUR)")
plt.title("Average Recommended Price by Product")
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y")
plt.savefig("graph_6_avg_price_by_product.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Demand_Index"], df["Price_Adjustment_Percentage"])
plt.xlabel("Demand Index")
plt.ylabel("Price Adjustment (%)")
plt.title("Demand Index vs Price Adjustment")
plt.grid(True)
plt.savefig("graph_7_demand_vs_adjustment.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Stock_Level"], df["Price_Adjustment_Percentage"])
plt.xlabel("Stock Level (%)")
plt.ylabel("Price Adjustment (%)")
plt.title("Stock Level vs Price Adjustment")
plt.grid(True)
plt.savefig("graph_8_stock_vs_adjustment.png", dpi=300, bbox_inches="tight")
plt.show()


print("All graphs have been created and saved successfully.")