import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Optional: Load external CSS
try:
    with open('css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except:
    pass

# Embedded CSS with modern tech UI and turquoise palette
st.markdown("""
    <style>
        /* Global reset & font */
        body, html {
            font-family: 'Segoe UI', sans-serif;
            background: #ecfdfd;
            color: #333;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #d1f2eb;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: #1abc9c;
            border-radius: 10px;
        }

        /* Main container */
        .main {
            max-width: 850px;
            margin: 0 auto;
            padding: 3rem 2rem;
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border-radius: 24px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.08);
        }

        /* Title */
        .title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #1abc9c;
            text-align: center;
            margin-bottom: 2.5rem;
            letter-spacing: -1px;
        }

        /* Selectbox input text color */
        .stSelectbox > div > div {
            color: #1a1a1a !important;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #1abc9c, #16a085);
            color: white;
            font-size: 1rem;
            font-weight: bold;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            transition: all 0.3s ease;
            margin-top: 1rem;
            box-shadow: 0 6px 20px rgba(26, 188, 156, 0.3);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            background: linear-gradient(135deg, #17a589, #148f77);
            box-shadow: 0 8px 24px rgba(26, 188, 156, 0.4);
        }

        /* Recommendation card */
        .card {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1.8rem 1.4rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(26, 188, 156, 0.15);
            transition: all 0.3s ease;
            border: 1px solid rgba(26, 188, 156, 0.2);
        }

        .card:hover {
            transform: scale(1.015);
            box-shadow: 0 12px 36px rgba(26, 188, 156, 0.25);
        }

        .card h4 {
            font-size: 1.4rem;
            font-weight: 700;
            color: #117A65;
            margin-bottom: 0.75rem;
        }

        /* Buy button inside card */
        .link-btn {
            background: #1abc9c;
            color: white !important;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-block;
        }

        .link-btn:hover {
            background: #148f77;
            transform: scale(1.05);
        }

        /* Image styling */
        img {
            border-radius: 18px;
            margin: 2rem auto 1rem auto;
            display: block;
            max-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Load data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommender logic
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [medicines.iloc[i[0]].Drug_Name for i in medicines_list]

# Main UI
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">💊 Smart Medicine Recommender</div>', unsafe_allow_html=True)
# Medicine image
image = Image.open('images/medicine-image.jpg')
st.image(image, caption='Recommended Medicines')

# Search input
selected_medicine_name = st.selectbox(
    '🔍 Enter your medicine name to get alternatives:',
    medicines['Drug_Name'].values
)

# Recommend button with icon
if st.button("🔎 Recommend"):
    with st.spinner("Finding alternatives..."):
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
