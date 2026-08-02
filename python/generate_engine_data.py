import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

output_file = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "aircraft_engine_data.csv"
)

output_file.parent.mkdir(exist_ok=True)

start_time = datetime(2026, 1, 1, 8, 0)
engines = ["ENG-001", "ENG-002", "ENG-003"]

rows = []

for engine_id in engines:
    flight_hours = random.randint(800, 2400)

    for reading_number in range(200):
        recorded_at = start_time + timedelta(minutes=5 * reading_number)

        temperature = round(random.normalvariate(710, 35), 2)
        oil_pressure = round(random.normalvariate(48, 5), 2)
        vibration = round(abs(random.normalvariate(3.2, 1.1)), 2)
        fuel_flow = round(random.normalvariate(2450, 180), 2)
        engine_speed = round(random.normalvariate(92, 4), 2)

        if temperature > 780 or oil_pressure < 38 or vibration > 5.5:
            status = "Critical"
        elif temperature > 750 or oil_pressure < 42 or vibration > 4.5:
            status = "Warning"
        else:
            status = "Normal"

        maintenance_required = (
            "Yes" if status == "Critical" or flight_hours > 2200 else "No"
        )

        rows.append([
            engine_id,
            recorded_at.strftime("%Y-%m-%d %H:%M:%S"),
            temperature,
            oil_pressure,
            vibration,
            fuel_flow,
            engine_speed,
            flight_hours,
            status,
            maintenance_required
        ])

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "engine_id",
        "recorded_at",
        "temperature_c",
        "oil_pressure_psi",
        "vibration_mm_s",
        "fuel_flow_kg_h",
        "engine_speed_percent",
        "flight_hours",
        "status",
        "maintenance_required"
    ])

    writer.writerows(rows)

print(f"Created {len(rows)} simulated readings.")
print(f"Saved to: {output_file}")