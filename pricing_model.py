def get_peak_hour_score(time_period):
    if time_period in ["Lunch Peak", "Dinner Peak"]:
        return 1.0
    elif time_period in ["Afternoon", "Evening"]:
        return 0.6
    else:
        return 0.3


def get_day_score(day_type):
    return 1.0 if day_type == "Weekend" else 0.6


def calculate_pricing_score(
    stock,
    demand_index,
    peak_hour_score,
    day_score,
    perishability
):
    stock_score = (100 - stock) / 100
    demand_score = demand_index / 100
    perishability_pressure = perishability * (stock / 100)

    pricing_score = (
        stock_score * 0.25 +
        demand_score * 0.40 +
        peak_hour_score * 0.15 +
        day_score * 0.10 -
        perishability_pressure * 0.10
    )

    return round(pricing_score, 3)


def calculate_price(base_price, cost, pricing_score, product_sensitivity):
    adjustment_percentage = (pricing_score - 0.50) * 0.40
    adjustment_percentage *= product_sensitivity

    recommended_price = base_price * (1 + adjustment_percentage)

    min_price = max(cost * 1.25, base_price * 0.85)
    max_price = base_price * 1.20

    recommended_price = max(min_price, recommended_price)
    recommended_price = min(max_price, recommended_price)

    final_adjustment_percentage = (
        (recommended_price - base_price) / base_price
    ) * 100

    if final_adjustment_percentage > 2:
        decision = "Increase Price"
    elif final_adjustment_percentage < -2:
        decision = "Decrease Price"
    else:
        decision = "Keep Price"

    profit_margin = ((recommended_price - cost) / recommended_price) * 100

    return (
        round(final_adjustment_percentage, 2),
        round(recommended_price, 2),
        decision,
        round(profit_margin, 2)
    )