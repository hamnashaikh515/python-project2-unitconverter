import streamlit as st

st.title("🔄 Unit Converter App")
st.markdown("### Converts Length, Weight & Time instantly")
st.write("Welcome! Select a category, enter a value & get the converted result in real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084
        elif unit == "Centimeters to inches":
            return value * 0.393701
        elif unit == "Inches to centimeters":
            return value / 0.393701

    elif category == "Weight":
        if unit == "Pounds to kilograms":
            return value * 0.453592
        elif unit == "Kilograms to pounds":
            return value / 0.453592
        elif unit == "Grams to ounces":
            return value * 0.035274
        elif unit == "Ounces to grams":
            return value / 0.035274
        elif unit == "Kilograms to stones":
            return value * 0.157473
        elif unit == "Stones to kilograms":
            return value / 0.157473

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters", "Centimeters to inches", "Inches to centimeters"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Pounds to kilograms", "Kilograms to pounds", "Grams to ounces", "Ounces to grams", "Kilograms to stones", "Stones to kilograms"])
elif category == "Time":
    unit = st.selectbox("⌛ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    converted_value = convert_units(category, value, unit)
    if converted_value is not None:
        st.write(f"The converted value is: {converted_value:.2f}")
    else:
        st.write("Please select a valid conversion option.")
