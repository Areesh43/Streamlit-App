import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

# in the terminal run: streamlit run dashboard.py
# if prompts you to enter email, just press enter/return
# if streamlit not recognized, run:
#   python -m streamlit run dashboard.py

st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "NASA'S APOD"]
)

df = pd.read_csv("biscayneBay_waterquality.csv")

with tab1:
    # ----- Raw Data Statistics --------
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    # ---- 2D Plot lines -------
    # Water temperatures
    fig1 = px.line(df,
                   x="Time",
                   y="Temperature (c)")
    st.plotly_chart(fig1)

    # Ph level
    fig2 = px.scatter(df,
                      x="ODO mg/L",
                      y="Temperature (c)",
                      color="pH")
    st.plotly_chart(fig2)

with tab3:
    # ---- 3D Plot line ------
    # Total Water Column for Latitude and Longitude
    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("Astronomy Picture of the Day")
    # TODO: call a function that generates the APOD
    url = "https://api.nasa.gov/planetary/apod/?api_key="
    response = apod_generator(url, os.getenv("NASA_API_KEY"))

    # TODO: using the streamlit methods
    #  display the APOD image, title, and other features

    # Title of the Image
    title = response["title"]
    st.write(title)

    # Printing out the Image
    image = response["url"]
    st.image(image)

    # Date the image was taken
    date = response["date"]
    st.write(date)

    # The Media Type of the Image
    media = response["media_type"]
    st.write("Media type: " + media)

    # Description of the image
    explanation = response["explanation"]
    st.write(explanation)

    # Copyright
    st.write(copyright)