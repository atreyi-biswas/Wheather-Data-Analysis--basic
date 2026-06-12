import urllib.request
import json
import sys
import time
import logging
import pandas as pd

# Constants and Configuration
CITIES = [
    {"name": "Mumbai", "latitude": 19.0760, "longitude": 72.8777},
    {"name": "Delhi", "latitude": 28.6139, "longitude": 77.2090},
    {"name": "Chennai", "latitude": 13.0827, "longitude": 80.2707},
    {"name": "Kolkata", "latitude": 22.5726, "longitude": 88.3639}
]

WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Drizzle: Light", 53: "Drizzle: Moderate", 55: "Drizzle: Dense intensity",
    56: "Freezing Drizzle: Light", 57: "Freezing Drizzle: Dense intensity",
    61: "Rain: Slight", 63: "Rain: Moderate", 65: "Rain: Heavy intensity",
    66: "Freezing Rain: Light", 67: "Freezing Rain: Heavy intensity",
    71: "Snow fall: Slight", 73: "Snow fall: Moderate", 75: "Snow fall: Heavy intensity",
    77: "Snow grains",
    80: "Rain showers: Slight", 81: "Rain showers: Moderate", 82: "Rain showers: Violent",
    85: "Snow showers: Slight", 86: "Snow showers: Heavy",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
}

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("weather_fetcher.log", encoding='utf-8')
    ]
)

def fetch_weather_for_city(city, retries=3, retry_delay=2):
    """
    Fetches raw weather JSON from Open-Meteo API for a single city.
    Includes a retry mechanism to handle transient network issues.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={city['latitude']}"
        f"&longitude={city['longitude']}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    )
    
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Fetching weather for {city['name']} (Attempt {attempt}/{retries})...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                if response.status != 200:
                    raise ValueError(f"HTTP error status: {response.status}")
                
                raw_data = response.read().decode('utf-8')
                parsed_data = json.loads(raw_data)
                return parsed_data
                
        except Exception as e:
            logging.warning(f"Error fetching data for {city['name']} on attempt {attempt}: {e}")
            if attempt < retries:
                time.sleep(retry_delay)
            else:
                logging.error(f"Failed to fetch data for {city['name']} after {retries} attempts.")
    return None

def process_weather_data(city, response_data):
    """
    Validates API response and extracts weather parameters into a standardized format.
    """
    if not response_data or "current" not in response_data:
        logging.error(f"Invalid API response format for {city['name']}.")
        return None
        
    current = response_data["current"]
    
    # Validate required data fields are present in API response
    required_keys = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "weather_code", "time"]
    for key in required_keys:
        if key not in current:
            logging.warning(f"Expected key '{key}' was missing in the API response for {city['name']}.")

    # Extract values safely
    temp = current.get("temperature_2m")
    wind_speed = current.get("wind_speed_10m")
    humidity = current.get("relative_humidity_2m")
    weather_code = current.get("weather_code")
    timestamp = current.get("time")
    
    condition_desc = WMO_CODES.get(weather_code, "Unknown") if weather_code is not None else None

    # Standardized column names in snake_case format
    return {
        "city_name": city["name"],
        "latitude": response_data.get("latitude", city["latitude"]),
        "longitude": response_data.get("longitude", city["longitude"]),
        "temperature_c": temp,
        "wind_speed_kmh": wind_speed,
        "humidity_pct": humidity,
        "weather_code": weather_code,
        "weather_condition": condition_desc,
        "timestamp_utc": timestamp
    }

def build_dataframe(processed_records):
    """
    Transforms list of records into a Pandas DataFrame and handles missing values.
    """
    if not processed_records:
        logging.warning("No weather records processed successfully. Returning empty DataFrame.")
        return pd.DataFrame()
        
    df = pd.DataFrame(processed_records)
    
    # Handle missing/null values explicitly using Pandas NA objects
    df["temperature_c"] = df["temperature_c"].fillna(pd.NA)
    df["wind_speed_kmh"] = df["wind_speed_kmh"].fillna(pd.NA)
    df["humidity_pct"] = df["humidity_pct"].fillna(pd.NA)
    df["weather_code"] = df["weather_code"].fillna(pd.NA)
    df["weather_condition"] = df["weather_condition"].fillna("Unknown")
    df["timestamp_utc"] = df["timestamp_utc"].fillna("N/A")
    
    return df

def save_to_csv(df, filepath):
    """
    Saves the DataFrame to a CSV file.
    """
    try:
        df.to_csv(filepath, index=False)
        logging.info(f"Successfully saved weather report to: {filepath}")
    except Exception as e:
        logging.error(f"Failed to write CSV file to {filepath}: {e}")

def main():
    processed_records = []
    
    for city in CITIES:
        try:
            # Fetch weather with individual city error handling
            raw_weather = fetch_weather_for_city(city)
            if raw_weather:
                record = process_weather_data(city, raw_weather)
                if record:
                    processed_records.append(record)
            else:
                logging.error(f"Skipping processing for {city['name']} due to fetch failure.")
        except Exception as err:
            logging.error(f"Unexpected error handling {city['name']}: {err}")
            
        # Add 1 second delay between calls to respect API limits
        time.sleep(1.0)
        
    # Build the final DataFrame
    df = build_dataframe(processed_records)
    
    if not df.empty:
        # Display the data frame in output logs
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        logging.info("Completed weather processing. Resulting DataFrame:")
        print("\n" + df.to_string(index=False) + "\n")
        
        # Save to CSV
        csv_file_path = "C:/Users/atrey/.gemini/antigravity/scratch/weather_report.csv"
        save_to_csv(df, csv_file_path)
    else:
        logging.critical("No weather data could be successfully retrieved and processed.")

if __name__ == "__main__":
    main()
