# Weather Data Analysis Pipeline

## Project Overview
This project is a Python-based weather data pipeline that fetches real-time weather data using an API, processes and cleans the data, and stores it in a structured format for further analysis. The project demonstrates a complete data engineering and data analytics workflow including data extraction, transformation, validation, and storage.

---

## Objective
- Fetch real-time weather data using an external API
- Process and clean raw JSON responses
- Build a structured dataset for analysis
- Implement error handling and retry mechanisms
- Store processed data in CSV format for downstream use
- Create a reusable and scalable data pipeline

---

## Data Source
- Open-Meteo API (https://open-meteo.com/)

---

## Tech Stack

| Technology | Contribution to Project |
|------------|------------------------|
| Python | Core programming language used to build the entire data pipeline |
| urllib / requests | Used to make API calls and fetch weather data from external sources |
| JSON | Used to parse and handle raw API responses |
| Pandas | Used for structuring, cleaning, and transforming data into DataFrames |
| Logging | Used to track execution flow, errors, and debugging information |
| CSV | Used to store processed weather data for further analysis and visualization |

---

## Cities Covered
- Mumbai
- Delhi
- Chennai
- Kolkata

---

## Project Workflow
1. Fetch weather data from API for multiple cities  
2. Implement retry mechanism for handling API failures  
3. Parse JSON response into structured format  
4. Extract required weather parameters:
   - Temperature
   - Wind Speed
   - Humidity
   - Weather Condition
   - Timestamp  
5. Validate and clean extracted data  
6. Convert data into Pandas DataFrame  
7. Handle missing or inconsistent values  
8. Export final dataset to CSV file  
9. Log execution details for monitoring and debugging  

---

## Features
- Multi-city weather data extraction
- Robust API error handling with retry mechanism
- Logging system for monitoring execution
- Data validation and cleaning pipeline
- Structured tabular output using Pandas
- CSV export for further analysis

---


## How to Run

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Run the script
python src/weather_pipeline.py

---

## Future Improvements
- Add data visualization using Matplotlib or Seaborn
- Build interactive dashboard using Power BI
- Include historical weather trend analysis
- Automate daily data collection using scheduling tools
- Deploy pipeline on cloud platforms

---

## Key Learning Outcomes
- API integration using Python
- Data extraction and transformation
- Error handling and retry mechanisms
- Logging and debugging practices
- Building end-to-end data pipelines
