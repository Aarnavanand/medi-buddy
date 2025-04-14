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
        /* Layout container */
        .main {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Title */
        .title {
            font-size: 3rem;
            font-weight: 700;
            color: #1ABC9C;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Input text color */
        .stSelectbox > div > div {
            color: white !important;
        }

        /* Button styling */
        .stButton > button {
            background-color: #1ABC9C;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            transition: background 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 1rem;
        }

        .stButton > button:hover {
            background-color: #17A589;
        }

        /* Card container */
        .card {
            background: linear-gradient(145deg, #f0fdfa, #d0f0e9);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 20px rgba(26, 188, 156, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(26, 188, 156, 0.2);
        }

        .card h4 {
            margin: 0 0 0.5rem 0;
            font-size: 1.3rem;
            color: #117A65;
        }

        /* Buy button inside card */
        .link-btn {
            display: inline-block;
            margin-top: 0.5rem;
            background-color: #1ABC9C;
            color: white !important;
            text-decoration: none !important;
            font-size: 0.95rem;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            transition: background 0.3s ease;
        }

        .link-btn:hover {
            background-color: #148F77;
            color: white;
        }

        /* Image styling */
        img {
            border-radius: 14px;
            margin-top: 2rem;
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
