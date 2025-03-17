import streamlit as st
from PIL import Image

# Theme settings for the app
st.set_page_config(
    page_title="Elegant Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add an image to the header
image = Image.open('header_image.jpg')  # Ensure this image exists in your project folder
st.image(image, use_container_width=True)

# App title and description
st.title('Elegant Unit Converter')
st.write('Convert between different units.')

# Selection box for unit category
option = st.sidebar.selectbox('Select Unit Category:', ('Length', 'Weight', 'Temperature', 'Time'))

# Input box for value
value = st.sidebar.number_input('Enter Value:', min_value=0.0, format="%.2f")

# Unit conversion functions
def length_converter(val, from_unit, to_unit):
    conversion_factors = {
        'Meter': 1,
        'Inch': 39.3701,
        'Kilometer': 0.001,
        'Mile': 0.000621371
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(val, from_unit, to_unit):
    conversion_factors = {
        'Kilogram': 1,
        'Pound': 2.20462
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(val, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (val * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (val - 32) * 5/9
    else:
        return val

def time_converter(val, from_unit, to_unit):
    conversion_factors = {
        'Second': 1,
        'Minute': 1/60,
        'Hour': 1/3600
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

# Input and output units based on the selected category
if option == 'Length':
    from_unit = st.selectbox('From Unit:', ('Meter', 'Inch', 'Kilometer', 'Mile'))
    to_unit = st.selectbox('To Unit:', ('Meter', 'Inch', 'Kilometer', 'Mile'))
    result = length_converter(value, from_unit, to_unit)
elif option == 'Weight':
    from_unit = st.selectbox('From Unit:', ('Kilogram', 'Pound'))
    to_unit = st.selectbox('To Unit:', ('Kilogram', 'Pound'))
    result = weight_converter(value, from_unit, to_unit)
elif option == 'Temperature':
    from_unit = st.selectbox('From Unit:', ('Celsius', 'Fahrenheit'))
    to_unit = st.selectbox('To Unit:', ('Celsius', 'Fahrenheit'))
    result = temperature_converter(value, from_unit, to_unit)
elif option == 'Time':
    from_unit = st.selectbox('From Unit:', ('Second', 'Minute', 'Hour'))
    to_unit = st.selectbox('To Unit:', ('Second', 'Minute', 'Hour'))
    result = time_converter(value, from_unit, to_unit)

# Display the result
st.success(f'Result: {value} {from_unit} = {result:.2f} {to_unit}')

# Add custom CSS
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
