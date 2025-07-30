from src.User import User 
from src.HealthMetric import HealthMetric
import csv
import pandas as pd
import matplotlib.pyplot as plt


user1 = User('garv',18,'male')

entries = [
    HealthMetric("2025-07-15", 4500, 1900, 6.0, "Tired"),
    HealthMetric("2025-07-16", 5200, 2100, 6.5, "Neutral"),
    HealthMetric("2025-07-17", 8100, 2500, 7.5, "Happy"),
    HealthMetric("2025-07-18", 3000, 1800, 5.0, "Low"),
    HealthMetric("2025-07-19", 7000, 2300, 6.8, "Good"),
    HealthMetric("2025-07-20", 6500, 2200, 7.0, "Neutral"),
    HealthMetric("2025-07-21", 9000, 2600, 8.0, "Happy"),
    HealthMetric("2025-07-22", 4000, 2000, 5.5, "Stressed"),
    HealthMetric("2025-07-23", 7500, 2400, 7.2, "Good"),
    HealthMetric("2025-07-24", 8300, 2550, 7.8, "Happy")
]




for entry in entries:
    user1.add_entry(entry)
user1.save_to_csv("data/Garv_Data.csv")
