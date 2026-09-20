import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('linear_regression_model.pkl')

# Load model columns
model_columns = joblib.load('model_columns.pkl')


# Page title
st.title("🚗 Used Car Price Prediction")

st.write("Enter the car details below to predict the estimated price.")


# User inputs
brand = st.selectbox(
    "Brand",
    ["Toyota", "Honda", "Ford", "BMW", "Audi"]
)

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2020
)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.5,
    max_value=10.0,
    value=2.0
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Electric"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=45000
)

condition = st.selectbox(
    "Condition",
    ["Good", "Excellent", "Fair", "Poor"]
)


# Prediction button
if st.button("Predict Price"):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Numerical values
    input_df["Year"] = year
    input_df["Engine Size"] = engine_size
    input_df["Mileage"] = mileage

    # Categorical values
    brand_col = "Brand_" + brand
    fuel_col = "Fuel Type_" + fuel_type
    transmission_col = "Transmission_" + transmission
    condition_col = "Condition_" + condition

    if brand_col in input_df.columns:
        input_df[brand_col] = 1

    if fuel_col in input_df.columns:
        input_df[fuel_col] = 1

    if transmission_col in input_df.columns:
        input_df[transmission_col] = 1

    if condition_col in input_df.columns:
        input_df[condition_col] = 1

    # Prediction
    prediction = model.predict(input_df)[0]

    st.success(
        f"Estimated Car Price: ₹{prediction:,.2f}"
    )