import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/weather_report.csv")

#Temperature by city
plt.figure()
plt.bar(df["city_name"], df["temperature_c"])
plt.title("Temperature by City", color='Purple', weight='bold')
plt.xlabel("City", color='red')
plt.ylabel("Temperature (°C)", color='red')
plt.savefig("output assets/temperature.png")
plt.show()

#Humidity by city
plt.figure()
plt.bar(df["city_name"], df["humidity_pct"])
plt.title("Humidity by City", color='Purple', weight='bold')
plt.xlabel("City", color='red')
plt.ylabel("Humidity (%)", color='red')
plt.savefig("output assets/humidity.png")
plt.show()

#Wind Speed by city
plt.figure()
plt.bar(df["city_name"], df["wind_speed_kmh"])
plt.title("Wind Speed by City", color='Purple', weight='bold')
plt.xlabel("City", color='red')
plt.ylabel("Wind Speed (km/h)", color='red')
plt.savefig("output assets/wind.png")
plt.show()


# Wheather condition count
condition_counts = df["weather_condition"].value_counts()

plt.figure()
plt.bar(condition_counts.index, condition_counts.values)
plt.title("Weather Condition Distribution", color='Purple', weight='bold')
plt.xlabel("Condition", color='red')
plt.ylabel("Count", color='red')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output assets/weather_conditions.png")
plt.show()

#Temperature by humidity
plt.figure()
plt.bar(df["temperature_c"], df["humidity_pct"], edgecolor='black')
plt.title("Temperature vs Humidity Relationship", color='Purple', weight='bold')
plt.xlabel("Temperature (°C)", color='red')
plt.ylabel("Humidity (%)", color='red')
plt.savefig("output assets/temp_vs_humidity.png")
plt.show()
