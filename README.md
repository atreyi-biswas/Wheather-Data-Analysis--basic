<h1 align="center">Weather Data Analysis Pipeline</h1>

<div align="center">

![Python](https://img.shields.io/badge/python-3670A1?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/powerbi-F2C811.svg?style=for-the-badge&logo=powerbi&logoColor=black)

</div>

## Overview
A Python weather data project that fetches current weather for Indian cities using the Open-Meteo API, cleans and structures the response data, and saves outputs for analysis and visualization.

## Repository Structure
## Repository Structure
- `src/wheather_pipeline.py` — fetches weather data, processes records, and saves `data/weather_report.csv`
- `analysis.py` — computes city summaries and saves `data/city_summary.csv`
- `visualization.py` — generates chart PNGs in `output assets/`
- `weather_visualizations.pbix` — Power BI dashboard for interactive weather data analysis
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
- Provides an interactive Power BI dashboard for weather insights and comparisons


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
5. Open the Power BI dashboard:
   ```bash
   weather_visualizations.pbix

   
## Output Files
- `data/weather_report.csv`
- `data/city_summary.csv`
- `output assets/temperature.png`
- `output assets/humidity.png`
- `output assets/wind.png`
- `output assets/weather_conditions.png`
- `output assets/temp_vs_humidity.png`
- `weather_visualizations.pbix`

## Notes
- The project uses Open-Meteo, which requires no API key
- Logging output is written to `weather_fetcher.log`
- The pipeline uses snake_case columns such as `temperature_c`, `humidity_pct`, and `wind_speed_kmh`

## Future Improvements
- Schedule regular daily data collection
- Expand supported cities and historical storage
- Add more derived metrics and trend analysis

