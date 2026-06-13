<h1 align="center">Weather Data Analysis Pipeline</h1><br>

## Overview
A Python weather data project that fetches current weather for Indian cities using the Open-Meteo API, cleans and structures the response data, and saves outputs for analysis and visualization.

## Repository Structure
- `src/wheather_pipeline.py` — fetches weather data, processes records, and saves `data/weather_report.csv`
- `analysis.py` — computes city summaries and saves `data/city_summary.csv`
- `visualization.py` — generates chart PNGs in `output assets/`
- `data/` — contains generated CSV output files
- `output assets/` — contains generated visualizations
- `logs/` — logging artifacts and project notes
- `weather_fetcher.log` — runtime logging for API fetches

## What it does
- Fetches current weather from Open-Meteo for Mumbai, Delhi, Chennai, and Kolkata
- Retries API calls on transient failures
- Extracts temperature, humidity, wind speed, weather condition, and timestamp
- Standardizes records into a Pandas DataFrame
- Handles missing values before export
- Saves cleaned data to CSV
- Produces analysis summaries and visualizations

## Dependencies
- Python 3.8+
- pandas
- matplotlib

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```
   or if using a requirements file:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the weather pipeline:
   ```bash
   python src/wheather_pipeline.py
   ```
3. Run analysis:
   ```bash
   python analysis.py
   ```
4. Generate visualizations:
   ```bash
   python visualization.py
   ```

## Output Files
- `data/weather_report.csv`
- `data/city_summary.csv`
- `output assets/temperature.png`
- `output assets/humidity.png`
- `output assets/wind.png`
- `output assets/weather_conditions.png`
- `output assets/temp_vs_humidity.png`

## Notes
- The project uses Open-Meteo, which requires no API key
- Logging output is written to `weather_fetcher.log`
- The pipeline uses snake_case columns such as `temperature_c`, `humidity_pct`, and `wind_speed_kmh`

## Future Improvements
- Add a dashboard or interactive visualization layer
- Schedule regular daily data collection
- Expand supported cities and historical storage
- Add more derived metrics and trend analysis

