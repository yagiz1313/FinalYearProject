import random
import csv

from sensor_processing import process_sensor_data
from pricing_model import (
    get_peak_hour_score,
    get_day_score,
    calculate_pricing_score,
    calculate_price
)


random.seed(42)

products = [
    ("Margherita Pizza", 12, 4.50, 1.10, 0.60),
    ("Pasta Carbonara", 14, 5.20, 1.00, 0.50),
    ("Lasagna", 15, 6.00, 1.00, 0.70),
    ("Risotto", 16, 6.50, 1.05, 0.55),
    ("Tiramisu", 7, 2.80, 0.85, 0.90),
    ("Espresso", 3, 0.70, 0.60, 0.20)
]

time_periods = [
    "Morning",
    "Lunch Peak",
    "Afternoon",
    "Dinner Peak",
    "Evening"
]

day_types = ["Weekday", "Weekend"]

filename = "smart_restaurant_pricing_sensor_based.csv"
dataset = []

for scenario_id in range(1, 101):
    product_name, base_price, cost, product_sensitivity, perishability = random.choice(products)

    sensor_data = process_sensor_data()

    stock = sensor_data["stock_level"]
    table_occupancy = sensor_data["table_occupancy"]
    customer_density = sensor_data["customer_density"]
    demand_index = sensor_data["demand_index"]

    time_period = random.choice(time_periods)
    day_type = random.choice(day_types)

    peak_hour_score = get_peak_hour_score(time_period)
    day_score = get_day_score(day_type)

    pricing_score = calculate_pricing_score(
        stock,
        demand_index,
        peak_hour_score,
        day_score,
        perishability
    )

    adjustment_percentage, recommended_price, decision, profit_margin = calculate_price(
        base_price,
        cost,
        pricing_score,
        product_sensitivity
    )

    dataset.append([
        scenario_id,
        product_name,
        base_price,
        cost,
        product_sensitivity,
        perishability,
        stock,
        table_occupancy,
        customer_density,
        demand_index,
        time_period,
        day_type,
        peak_hour_score,
        day_score,
        pricing_score,
        adjustment_percentage,
        recommended_price,
        decision,
        profit_margin
    ])


with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Scenario_ID",
        "Product_Name",
        "Base_Price_EUR",
        "Cost_EUR",
        "Product_Sensitivity",
        "Perishability",
        "Stock_Level",
        "Table_Occupancy_Percentage",
        "Customer_Density_Percentage",
        "Demand_Index",
        "Time_Period",
        "Day_Type",
        "Peak_Hour_Score",
        "Day_Score",
        "Pricing_Score",
        "Price_Adjustment_Percentage",
        "Recommended_Price_EUR",
        "Decision",
        "Profit_Margin_Percentage"
    ])

    writer.writerows(dataset)


print("Sensor-based smart pricing dataset created successfully.")
print(f"File name: {filename}")
print(f"Total scenarios: {len(dataset)}")