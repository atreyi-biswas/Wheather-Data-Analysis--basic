import pandas as pd
import logging

df = pd.read_csv("data/weather_report.csv")

# Average Temperature per city
print(df.groupby("city_name")["temperature_c"].mean())

# Average Humidity per city
print(df.groupby("city_name")["humidity_pct"].mean())

# Average Wind Speed per city
print(df.groupby("city_name")["wind_speed_kmh"].mean())

# Maximum and Minimum temperature rows
max_temp_row = df.loc[df["temperature_c"].idxmax()]
min_temp_row = df.loc[df["temperature_c"].idxmin()]

print(max_temp_row)
print(min_temp_row)

# Summary table
summary = df.groupby("city_name").agg({
    "temperature_c": "mean",
    "humidity_pct": "mean",
    "wind_speed_kmh": "mean"
}).reset_index()

summary.to_csv("data/city_summary.csv", index=False)

# Insights
print("\nCITY ANALYSIS SUMMARY")
print(summary)

print("\nHIGHEST TEMPERATURE(amongst all cities):")
print(f"{max_temp_row['city_name']} - {max_temp_row['temperature_c']}°C")

print("\nLOWEST TEMPERATURE(amongst all cities):")
print(f"{min_temp_row['city_name']} - {min_temp_row['temperature_c']}°C")


#City-wise max min
city_max_temps = df.groupby("city_name")["temperature_c"].max()
city_min_temps = df.groupby("city_name")["temperature_c"].min()

print("\nCITY-WISE MAXIMUM TEMPERATURES:")
print(city_max_temps)

print("\nCITY-WISE MINIMUM TEMPERATURES:")
print(city_min_temps)

#LOGGING
logging.info(
    f"HIGHEST TEMP: {max_temp_row['city_name']} - {max_temp_row['temperature_c']}°C"
)

logging.info(
    f"LOWEST TEMP: {min_temp_row['city_name']} - {min_temp_row['temperature_c']}°C"
)