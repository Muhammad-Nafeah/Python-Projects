import streamlit as st

# Conversion factors (base units are in SI units)
conversion_factors = {
    "Area": {
        "Square kilometer": 1e6,  # Base unit: square meter
        "Square meter": 1,
        "Square mile": 2.59e6,
        "Square yard": 0.836127,
        "Square foot": 0.092903,
        "Square inch": 0.00064516
    },
    "Data Transfer Rate": {
        "Bit per second": 1,  # Base unit: bit per second
        "Kilobit per second": 1000,
        "Byte per second": 8
    },
    "Energy": {
        "Joule": 1,  # Base unit: joule
        "Kilojoule": 1000,
        "Gram calorie": 4.184,
        "Kilocalorie": 4184,
        "Kilowatt-hour": 3.6e6
    },
    "Frequency": {
        "Hertz": 1,  # Base unit: hertz
        "Kilohertz": 1e3,
        "Megahertz": 1e6,
        "Gigahertz": 1e9
    },
    "Length": {
        "Kilometer": 1000,  # Base unit: meter
        "Meter": 1,
        "Centimeter": 0.01,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    },
    "Mass": {
        "Tonne": 1000,  # Base unit: kilogram
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    },
    "Pressure": {
        "Bar": 100000,  # Base unit: pascal
        "Pascal": 1,
        "Pound per square inch": 6894.76,
        "Torr": 133.322
    },
    "Speed": {
        "Mile per hour": 0.44704,  # Base unit: meter per second
        "Foot per second": 0.3048,
        "Meter per second": 1,
        "Kilometer per hour": 0.277778
    },
    "Temperature": "special",  # Special case for temperature conversion
    "Time": {
        "Nanosecond": 1e-9,  # Base unit: second
        "Microsecond": 1e-6,
        "Millisecond": 1e-3,
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2.628e6,  # Approximate (30.44 days)
        "Year": 3.154e7  # Approximate (365.25 days)
    },
    "Volume": {
        "Liter": 1,  # Base unit: liter
        "Milliliter": 0.001
    }
}
def convert_unit(value,from_unit, to_unit,category):
    if category not in conversion_factors:
        return "Invalid Category"
    
    if category == "Temperature":
        if from_unit == "Degree Celcius" and to_unit == "Fehrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Degree Celcius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fehrenheit" and to_unit == "Degree Celcius":
            return (value - 32) * 5/9
        elif from_unit == "Fehrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Degree Celcius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fehrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return "Invalid Conversion"
    
    # Step 1: Convert from input unit to base unit
    base_unit = value * conversion_factors[category][from_unit]
    # Step 2: Convert from base unit to output unit
    converted_value = base_unit / conversion_factors[category][to_unit]

    return converted_value

unit_options = {
    "Area" : ["Square kilometer","Square meter","Square mile","Square yard","Square foot","Square inch"],
    "Data Transfer Rate" : ["Bit per second","Kilobit per second","byte per second"],
    "Energy":["Joule","kilojoule","Gram calorie","Kilocalorie","Kilowatt-hour"],
    "Frequency" : ["Hertz","Kilohertz" , "Megahertz" , "Gigahertz"],
    "Length" : ["Kilometer","Meter","Centimeter","Mile","Yard","Foot","Inch"],
    "Mass" : ["Tonne","Kilogram","Gram","Milligram","Pound","Ounce"],
    "Pressure" : ["Bar","Pascal","Pound per square inch","Torr"],
    "Speed" : ["Mile per hour","foot per second", "Meter per second" ,"Kilometer per hour"],
    "Temperature" : ["Degree Celcius","Fehrenheit","Kelvin"],
    "Time" : ["Nanosecond","Microsecond","Millisecond","Second","Minute","Hour","Day","Week","Month","Year"],
    "Volume" : ["Liter","Milliliter"]
}
units = list(unit_options.keys())

category = st.selectbox("Select Category:", units , index=4)

selected_category = unit_options[category]

col1 ,col2 ,col3 = st.columns([4,1,4])

with col1:
    from_unit_selectbox = st.selectbox("",selected_category,key="from_selectbox",index = 0)
    from_unit_input = st.number_input("",value=1,key="from_unit")

with col2:
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 100%; padding-top: 50px'><h2>=</h2></div>", unsafe_allow_html=True)

with col3:
    to_unit_selectbox = st.selectbox("",selected_category,key="to_selectbox",index = 0)
    converted_value = convert_unit(from_unit_input,from_unit_selectbox,to_unit_selectbox,category)
    
    if isinstance(converted_value, (int, float)):  # Only format if numeric
        formatted_value = f"{converted_value:.2f} {to_unit_selectbox}"
    else:
        formatted_value = ""

    st.text_input("", formatted_value)

    











