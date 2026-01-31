# Water Quality Dashboard and NASA's APOD

## Purpose
The **Water Quality Dashboard** is an interactive Streamlit web application designed to visualize and explore environmental water quality data from **Biscayne Bay**.  
The application demonstrates skills in **data analysis, interactive visualization, and API integration**, and was developed for the *Internship Ready Software Development* course.

Users can:
- View raw water quality data and descriptive statistics
- Explore 2D and 3D visualizations
- Interact with NASA’s *Astronomy Picture of the Day (APOD)* API


## Dataset Used
**Biscayne Bay Water Quality Dataset** (`biscayneBay_waterquality.csv`)

This dataset contains environmental and geospatial measurements related to water conditions in Biscayne Bay.

### Key Columns
- **Time** – Timestamp of data collection  
- **Temperature (°C)** – Water temperature  
- **pH** – Acidity/alkalinity of the water  
- **ODO (mg/L)** – Dissolved oxygen levels  
- **Latitude & Longitude** – Geographic coordinates  
- **Total Water Column (m)** – Water depth measurement  

The dataset is used for descriptive statistics and visualization across multiple dimensions.

---

## Application Features

### Descriptive Statistics
- Displays the full dataset in a table
- Shows summary statistics including mean, min, max, and standard deviation

### 2D Visualizations
- Line chart of **Water Temperature vs Time**
- Scatter plot comparing **Dissolved Oxygen vs Temperature**, colored by pH

### 3D Visualization
- 3D scatter plot of **Longitude, Latitude, and Total Water Column**
- Depth axis is reversed to reflect real-world water columns

### NASA APOD Integration
- Uses NASA’s *Astronomy Picture of the Day* API
- User-selectable display options:
  - Image only
  - Image + Title
  - Image + Description
  - Full details (image, title, date, media type, description)


## How to Run the Application

### Install Dependencies
Make sure Python is installed, then run:

```bash
pip install streamlit pandas plotly
