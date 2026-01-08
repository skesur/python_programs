# Build a Streamlit app with:
# - Sidebar to select a country from a dropdown (India, USA, UK, Canada)
# - Number input for Total Population
# - Number input for Vaccinated People
# - A button that, when clicked, calculates and displays the vaccination percentage
# - Display results with a progress bar and a success/warning message depending on whether the vaccination rate is above
# 70%

import streamlit as st
import time as t

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="",
    layout="wide"
)

st.sidebar.title("Stramlit Topics")
page = st.sidebar.selectbox("Select A Country : ",["India","USA","UK","Canada"])

p=st.number_input("Enter Total Population: ")
v=st.number_input("Enter Vaccine Population: ")

if st.button("Vaccination Percentage"):
    progress = st.progress(0)
    with st.spinner("Processing..."):
        for i in range(100):
            t.sleep(0.05)
            progress.progress(i+1)
    per = (v/p)*100
    if per>70:
        st.success(f"Vaccination Percentage of {page} : {per}")
    else:
        st.warning(f"Vaccination Percentage of {page} : {per}")     
