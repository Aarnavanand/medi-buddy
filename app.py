import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Embedded CSS with modern glassmorphism and turquoise palette
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

        body {
            background: linear-gradient(135deg, #e0f7f5, #d1f2eb);
        }

        .main {
            max-width: 850px;
            margin: 0 auto;
            padding: 3rem 2rem;
            font-family: 'Poppins', sans-serif;
            background-color: rgba(255, 255, 255, 0.75);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.1);
            backdrop-filter: blur(10px);
        }

        .title {
            font-size: 3rem;
            font-weight: 700;
            color: #138D75;
            text-align: center;
            margin-bottom: 2rem;
        }

        .stSelectbox > div > div {
            color: #212121 !important;
        }

        .stButton > button {
            background: linear-gradient(90deg, #1ABC9C, #16A085);
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 50px;
            transition: all 0.3s ease;
            margin-top: 1rem;
            box-shadow: 0 4px 12px rgba(26, 188, 156, 0.3);
        }

        .stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #16A085, #1ABC9C);
        }

        .card {
            background: rgba(255, 255, 255, 0.6);
            border: 1px solid #e0e0e0;
            border-radius: 18px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            transition: 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card h4 {
            font-size: 1.4rem;
            color: #117A65;
            margin-bottom: 0.6rem;
        }

        .link-btn {
            background-color: #1ABC9C;
            color: white !important;
            text-decoration: none !important;
            font-size: 0.95rem;
            padding: 0.6rem 1.1rem;
            border-radius: 8px;
            transition: background 0.3s ease;
            display: inline-block;
        }

        .link-btn:hover {
            background-color: #148F77;
        }

        img {
            border-radius: 20px;
            margin-top: 1.5rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Load data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation logic
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [medicines.iloc[i[0]].Drug_Name for i in medicines_list]

# Main UI
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">💊 Smart Medicine Recommender</div>', unsafe_allow_html=True)

# HD Image
image_url = "https://images.unsplash.com/photo-1588776814546-ec7e75f8423a?auto=format&fit=crop&w=900&q=80"
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
st.image(img, caption="Stay Informed. Stay Safe.", use_column_width=True)

# Selectbox
selected_medicine_name = st.selectbox(
    '🔍 Select your medicine to get alternatives:',
    medicines['Drug_Name'].values
)

# Button and results
if st.button("🔎 Recommend"):
    recommendations = recommend(selected_medicine_name)
    for idx, med in enumerate(recommendations, start=1):
        st.markdown(f"""
            <div class="card">
                <h4>{idx}. {med}</h4>
                <a class="link-btn" href="https://pharmeasy.in/search/all?name={med}" target="_blank">
                    Buy on PharmEasy
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
