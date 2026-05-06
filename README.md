# Smart Restaurant Dynamic Pricing System

A sensor-driven dynamic pricing engine for restaurants that adjusts menu prices in real time based on occupancy, stock levels, demand, time of day, and day type.

---

## Overview

This project simulates a smart pricing system for a restaurant. It reads simulated sensor data (customer count, table occupancy, stock levels), computes a demand-driven pricing score, and recommends price adjustments for each menu item. Results can be visualized live or exported to a CSV dataset for analysis.

---

## Project Structure

```
codes/
├── sensor_processing.py      # Simulates and processes sensor data
├── pricing_model.py          # Scoring and price calculation logic
├── dataset_generator.py      # Generates a 100-scenario CSV dataset
├── live_price_simulation.py  # Runs a live 30-step price simulation with charts
└── graph_analysis.py         # Reads the CSV and produces analysis graphs
```

---

## Modules

### `sensor_processing.py`
Simulates IoT sensor readings for a restaurant environment and computes derived metrics:

| Function | Description |
|---|---|
| `simulate_sensor_data()` | Generates random values for people count, table occupancy, and stock |
| `calculate_customer_density()` | People count as a % of max capacity |
| `calculate_table_occupancy()` | Occupied tables as a % of total tables |
| `calculate_stock_level()` | Current stock as a % of max stock |
| `calculate_demand_index()` | Weighted combination of density (70%) and occupancy (30%) |
| `process_sensor_data()` | Runs all of the above and returns a dict of metrics |

---

### `pricing_model.py`
Contains the core pricing logic:

| Function | Description |
|---|---|
| `get_peak_hour_score(time_period)` | Returns 1.0 for peak hours, 0.6 for mid, 0.3 for off-peak |
| `get_day_score(day_type)` | Returns 1.0 for weekends, 0.6 for weekdays |
| `calculate_pricing_score(...)` | Weighted score combining stock, demand, peak hour, day, and perishability |
| `calculate_price(...)` | Converts the score into a final price with min/max guardrails |

**Pricing score weights:**

| Factor | Weight |
|---|---|
| Stock scarcity | 25% |
| Demand index | 40% |
| Peak hour score | 15% |
| Day score | 10% |
| Perishability pressure | −10% |

**Price bounds:**
- Minimum: `max(cost × 1.25, base_price × 0.85)`
- Maximum: `base_price × 1.20`

**Decision thresholds:**
- Adjustment > +2% → `Increase Price`
- Adjustment < −2% → `Decrease Price`
- Otherwise → `Keep Price`

---

### `dataset_generator.py`
Generates 100 randomised pricing scenarios and saves them to a CSV file:

**Output file:** `smart_restaurant_pricing_sensor_based.csv`

Each row represents one scenario with 19 columns including product details, sensor readings, scoring inputs, and the final pricing decision.

**Menu items included:**

| Product | Base Price | Cost |
|---|---|---|
| Margherita Pizza | €12.00 | €4.50 |
| Pasta Carbonara | €14.00 | €5.20 |
| Lasagna | €15.00 | €6.00 |
| Risotto | €16.00 | €6.50 |
| Tiramisu | €7.00 | €2.80 |
| Espresso | €3.00 | €0.70 |

---

### `live_price_simulation.py`
Runs a 30-step real-time simulation. At each step:
- New sensor data is generated
- A random time period and day type are selected
- Prices are calculated for all 6 products
- A live matplotlib chart is updated showing price evolution over time

---

### `graph_analysis.py`
Reads the generated CSV and produces 8 saved analysis graphs:

| File | Chart |
|---|---|
| `graph_1_demand_vs_price.png` | Demand Index vs Recommended Price |
| `graph_2_stock_vs_price.png` | Stock Level vs Recommended Price |
| `graph_3_score_vs_adjustment.png` | Pricing Score vs Price Adjustment |
| `graph_4_decision_distribution.png` | Distribution of Pricing Decisions |
| `graph_5_avg_adjustment_by_product.png` | Average Adjustment by Product |
| `graph_6_avg_price_by_product.png` | Average Recommended Price by Product |
| `graph_7_demand_vs_adjustment.png` | Demand Index vs Price Adjustment |
| `graph_8_stock_vs_adjustment.png` | Stock Level vs Price Adjustment |

---

## Requirements

```
matplotlib
pandas
```

Install with:
```bash
pip install matplotlib pandas
```

No external data sources or APIs are required — all sensor data is simulated internally.

---

## Usage

### 1. Generate the dataset
```bash
python dataset_generator.py
```
Creates `smart_restaurant_pricing_sensor_based.csv` in the working directory.

### 2. Run the live simulation
```bash
python live_price_simulation.py
```
Opens a live-updating chart showing price changes over 30 time steps.

### 3. Analyse the dataset
```bash
python graph_analysis.py
```
Reads the CSV and saves 8 graph images to the working directory.

> **Note:** Run `dataset_generator.py` before `graph_analysis.py`, as the latter requires the CSV file to exist.

---

## How the Pricing Score Works

```
pricing_score = (stock_score × 0.25)
              + (demand_score × 0.40)
              + (peak_hour_score × 0.15)
              + (day_score × 0.10)
              - (perishability_pressure × 0.10)
```

A score above 0.50 pushes prices up; below 0.50 pushes them down. The sensitivity parameter per product scales how aggressively the price reacts to the score.
