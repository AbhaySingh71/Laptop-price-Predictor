import streamlit as st
import pickle
import numpy as np

# Load model and data
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipeline.pkl', 'rb'))

st.set_page_config(page_title="Laptop Price Predictor", layout="wide")

# CSS styles without white container
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #0f4c81;
        text-align: center;
        margin-top: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #444;
    }
    .center-img {
        display: block;
        margin: 20px auto 10px auto;
        width: 100px;
    }
    div.stButton > button:first-child {
        background-color: #0f4c81;
        color: white;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #06426b;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Centered image and title (no white box)
st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/679/679720.png" class="center-img">', unsafe_allow_html=True)
st.markdown('<h1 class="title">💻 Laptop Price Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select your laptop specs and get an instant price estimate!</p>', unsafe_allow_html=True)

# Input form
with st.form("predict_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        company = st.selectbox("Brand", sorted(df['Company'].unique()))
        ram = st.selectbox("RAM (GB)", [2,4,6,8,12,16,24,32,64])
        touchscreen = st.radio("Touchscreen", ['No', 'Yes'], horizontal=True)
        resolution = st.selectbox(
            "Screen Resolution",
            ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
        )
        hdd = st.selectbox("HDD (GB)", [0,128,256,512,1024,2048])

    with col2:
        laptop_type = st.selectbox("Type", sorted(df['TypeName'].unique()))
        weight = st.number_input("Weight (kg)", 0.5, 5.0, 1.5, 0.1)
        ips = st.radio("IPS Display", ['No', 'Yes'], horizontal=True)
        screen_size = st.slider("Screen Size (inches)", 10.0, 18.0, 13.0, 0.1)
        ssd = st.selectbox("SSD (GB)", [0,8,128,256,512,1024])

    with col3:
        cpu = st.selectbox("CPU Brand", sorted(df['Cpu brand'].unique()))
        gpu = st.selectbox("GPU Brand", sorted(df['Gpu brand'].unique()))
        os = st.selectbox("Operating System", sorted(df['os'].unique()))
        st.write(" ")  # Spacer
        submit = st.form_submit_button("Predict Price 💰")

# Prediction logic
if submit:
    touchscreen_flag = 1 if touchscreen == 'Yes' else 0
    ips_flag = 1 if ips == 'Yes' else 0
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    features = np.array([[company, laptop_type, ram, weight, touchscreen_flag, ips_flag, ppi, cpu, hdd, ssd, gpu, os]])
    price_log = pipe.predict(features)[0]
    price = int(np.exp(price_log))

    st.markdown(f"""
        <div style="
            background-color:#dff0d8;
            border: 2px solid #3c763d;
            border-radius: 12px;
            padding: 15px;
            margin-top: 20px;
            max-width: 900px;
            font-size: 1.8rem;
            font-weight: 600;
            color: #3c763d;
            text-align: center;
            margin-left: auto;
            margin-right: auto;
            ">
            Estimated Laptop Price: ₹{price:,}
        </div>
    """, unsafe_allow_html=True)
