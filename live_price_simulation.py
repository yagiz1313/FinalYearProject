import random
import matplotlib.pyplot as plt

from sensor_processing import process_sensor_data
from pricing_model import (
    get_peak_hour_score,
    get_day_score,
    calculate_pricing_score,
    calculate_price
)

products = [
    {"name": "Margherita Pizza", "base_price": 12, "cost": 4.5, "sensitivity": 1.1, "perishability": 0.6},
    {"name": "Pasta Carbonara", "base_price": 14, "cost": 5.2, "sensitivity": 1.0, "perishability": 0.5},
    {"name": "Lasagna", "base_price": 15, "cost": 6.0, "sensitivity": 1.0, "perishability": 0.7},
    {"name": "Risotto", "base_price": 16, "cost": 6.5, "sensitivity": 1.05, "perishability": 0.55},
    {"name": "Tiramisu", "base_price": 7, "cost": 2.8, "sensitivity": 0.85, "perishability": 0.9},
    {"name": "Espresso", "base_price": 3, "cost": 0.7, "sensitivity": 0.6, "perishability": 0.2}
]

time_periods = ["Morning", "Lunch Peak", "Afternoon", "Dinner Peak", "Evening"]
day_types = ["Weekday", "Weekend"]

# Her ürün için ayrı price listesi
price_history = {product["name"]: [] for product in products}
time_steps = []

plt.ion()

for t in range(1, 31):
    sensor = process_sensor_data()

    stock = sensor["stock_level"]
    demand = sensor["demand_index"]

    time_period = random.choice(time_periods)
    day_type = random.choice(day_types)

    peak = get_peak_hour_score(time_period)
    day = get_day_score(day_type)

    time_steps.append(t)

    print(f"\n===== Time Step {t} =====")

    for product in products:
        score = calculate_pricing_score(
            stock,
            demand,
            peak,
            day,
            product["perishability"]
        )

        adjustment, price, decision, margin = calculate_price(
            product["base_price"],
            product["cost"],
            score,
            product["sensitivity"]
        )

        price_history[product["name"]].append(price)

        print(f"{product['name']}")
        print(f"Price: {price} EUR | Decision: {decision}")
        print("-" * 20)

    # Grafik güncelle
    plt.clf()

    for product in products:
        plt.plot(
            time_steps,
            price_history[product["name"]],
            marker="o",
            label=product["name"]
        )

    plt.xlabel("Time Step")
    plt.ylabel("Price (EUR)")
    plt.title("Live Price Change - All Products")
    plt.legend()
    plt.grid(True)

    plt.pause(1)

plt.ioff()
plt.show()