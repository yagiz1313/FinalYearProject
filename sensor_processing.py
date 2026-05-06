import random


def calculate_customer_density(people_count, max_capacity):
    density = (people_count / max_capacity) * 100
    return round(min(density, 100), 2)


def calculate_table_occupancy(occupied_tables, total_tables):
    occupancy = (occupied_tables / total_tables) * 100
    return round(min(occupancy, 100), 2)


def calculate_stock_level(current_stock, max_stock):
    stock_level = (current_stock / max_stock) * 100
    return round(min(stock_level, 100), 2)


def calculate_demand_index(customer_density, table_occupancy):
    demand_index = (customer_density * 0.7) + (table_occupancy * 0.3)
    return round(demand_index, 2)


def simulate_sensor_data():
    people_count = random.randint(5, 80)
    max_capacity = 80

    occupied_tables = random.randint(2, 20)
    total_tables = 20

    current_stock = random.uniform(5, 50)
    max_stock = 50

    return {
        "people_count": people_count,
        "max_capacity": max_capacity,
        "occupied_tables": occupied_tables,
        "total_tables": total_tables,
        "current_stock": current_stock,
        "max_stock": max_stock
    }


def process_sensor_data():
    raw_data = simulate_sensor_data()

    customer_density = calculate_customer_density(
        raw_data["people_count"],
        raw_data["max_capacity"]
    )

    table_occupancy = calculate_table_occupancy(
        raw_data["occupied_tables"],
        raw_data["total_tables"]
    )

    stock_level = calculate_stock_level(
        raw_data["current_stock"],
        raw_data["max_stock"]
    )

    demand_index = calculate_demand_index(
        customer_density,
        table_occupancy
    )

    return {
        "stock_level": stock_level,
        "table_occupancy": table_occupancy,
        "customer_density": customer_density,
        "demand_index": demand_index
    }