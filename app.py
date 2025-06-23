import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(page_title="🌍 World Population Sunburst", layout="wide")
st.title("🌍 World Population Breakdown - Sunburst Chart")

# Load the CSV data
@st.cache_data
def load_data():
    return pd.read_csv("world_population.csv")  # Make sure this file is in the same directory

df = load_data()

# Build the sunburst chart
fig = px.sunburst(
    df,
    path=["Continent", "Country", "State", "City"],
    values="Population",
    color="Continent",
    title="World Population by Continent → Country → State → City"
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Show raw data (optional)
with st.expander("📄 View Raw Data"):
    st.dataframe(df)
