import streamlit as st
from PIL import Image

# ایپ کے لیے تھیم سیٹنگز
st.set_page_config(
    page_title="دلکش یونٹ کنورٹر",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ہیڈر میں تصویر شامل کریں
image = Image.open('header_image.jpg')  # یقینی بنائیں کہ یہ تصویر آپ کے پروجیکٹ فولڈر میں موجود ہے
st.image(image, use_container_width=True)

# ایپ کا عنوان اور تفصیل
st.title('دلکش یونٹ کنورٹر')
st.write('مختلف یونٹس کے درمیان تبدیلی کریں۔')

# سلیکشن باکس برائے یونٹ کیٹیگری
option = st.sidebar.selectbox('یونٹ کیٹیگری منتخب کریں:', ('لمبائی', 'وزن', 'درجہ حرارت', 'وقت'))

# انپٹ باکس برائے ویلیو
value = st.sidebar.number_input('ویلیو درج کریں:', min_value=0.0, format="%.2f")

# یونٹ کنورژن فنکشنز
def length_converter(val, from_unit, to_unit):
    conversion_factors = {
        'میٹر': 1,
        'انچ': 39.3701,
        'کلومیٹر': 0.001,
        'میل': 0.000621371
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(val, from_unit, to_unit):
    conversion_factors = {
        'کلوگرام': 1,
        'پاؤنڈ': 2.20462
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(val, from_unit, to_unit):
    if from_unit == 'سیلسیئس' and to_unit == 'فارن ہائیٹ':
        return (val * 9/5) + 32
    elif from_unit == 'فارن ہائیٹ' and to_unit == 'سیلسیئس':
        return (val - 32) * 5/9
    else:
        return val

def time_converter(val, from_unit, to_unit):
    conversion_factors = {
        'سیکنڈ': 1,
        'منٹ': 1/60,
        'گھنٹے': 1/3600
    }
    return val * conversion_factors[to_unit] / conversion_factors[from_unit]

# یونٹ کیٹیگری کے مطابق انپٹ اور آؤٹ پٹ یونٹس
if option == 'لمبائی':
    from_unit = st.selectbox('سے یونٹ:', ('میٹر', 'انچ', 'کلومیٹر', 'میل'))
    to_unit = st.selectbox('تک یونٹ:', ('میٹر', 'انچ', 'کلومیٹر', 'میل'))
    result = length_converter(value, from_unit, to_unit)
elif option == 'وزن':
    from_unit = st.selectbox('سے یونٹ:', ('کلوگرام', 'پاؤنڈ'))
    to_unit = st.selectbox('تک یونٹ:', ('کلوگرام', 'پاؤنڈ'))
    result = weight_converter(value, from_unit, to_unit)
elif option == 'درجہ حرارت':
    from_unit = st.selectbox('سے یونٹ:', ('سیلسیئس', 'فارن ہائیٹ'))
    to_unit = st.selectbox('تک یونٹ:', ('سیلسیئس', 'فارن ہائیٹ'))
    result = temperature_converter(value, from_unit, to_unit)
elif option == 'وقت':
    from_unit = st.selectbox('سے یونٹ:', ('سیکنڈ', 'منٹ', 'گھنٹے'))
    to_unit = st.selectbox('تک یونٹ:', ('سیکنڈ', 'منٹ', 'گھنٹے'))
    result = time_converter(value, from_unit, to_unit)

# نتیجہ دکھائیں
st.success(f'نتیجہ: {value} {from_unit} = {result:.2f} {to_unit}')

# کسٹم CSS شامل کریں
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