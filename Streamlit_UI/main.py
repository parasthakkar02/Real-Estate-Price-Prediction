import streamlit as st
from helpers import get_locations, predict_price_function

with st.spinner("Processing. Please wait..."):
    locations = get_locations()

st.title("Bangalore House Price Predictor")

with st.form(key="repp_form"):
    area = st.number_input(
        label="Area (Square feet) :",
        min_value=100,
        step=1,
        format="%d",
        placeholder="Enter House Area in sq.ft.",
        value=500,
    )
    bhk = st.radio("Bedrooms :", options=[1, 2, 3, 4, 5], index=1, horizontal=True)
    bath = st.radio("Bathrooms :", options=[1, 2, 3, 4, 5], index=1, horizontal=True)
    location = st.selectbox("Locations", locations, index=None)
    submit = st.form_submit_button()

if submit:
    if not location:
        st.error("Please select a valid location.")
        st.stop()

    result = predict_price_function(location, area, bhk, bath)

    st.info(f"Result: {result} lacs")
