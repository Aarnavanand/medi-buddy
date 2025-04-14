import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Set page configuration for a wider layout and hospital-like theme
st.set_page_config(page_title="Smart Medicine Recommender", layout="wide", page_icon="💊")

# Embedded CSS with modern hospital-tech UI
st.markdown("""
    <style>
        /* Global reset & font */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body, html {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e0f7fa 100%);
            color: #2d3748;
            line-height: 1.6;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #e6ecf0;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb {
            background: #4a90e2;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #357abd;
        }

        /* Main container */
        .main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 2.5rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* Title */
        .title {
            font-size: 2.8rem;
            font-weight: 700;
            color: #2b6cb0;
            text-align: center;
            margin-bottom: 1.5rem;
            letter-spacing: -0.5px;
            background: linear-gradient(to right, #2b6cb0, #4a90e2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Subtitle */
        .subtitle {
            font-size: 1.2rem;
            color: #718096;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Selectbox styling */
        .stSelectbox {
            background: #ffffff;
            border-radius: 12px;
            padding: 0.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        .stSelectbox > div > div {
            color: #2d3748 !important;
            font-size: 1.1rem;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #4a90e2, #2b6cb0);
            color: white;
            font-size: 1.1rem;
            font-weight: 600;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 12px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(74, 144, 226, 0.3);
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #357abd, #1a4971);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(74, 144, 226, 0.5);
        }

        /* Recommendation card */
        .card {
            background: linear-gradient(145deg, #ffffff, #f7fafc);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 4px solid #4a90e2;
        }
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        }
        .card h4 {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 0.5rem;
        }
        .card p {
            font-size: 1rem;
            color: #718096;
            margin-bottom: 1rem;
        }

        /* Buy button inside card */
        .link-btn {
            background: #4a90e2;
            color: white !important;
            padding: 0.6rem 1.4rem;
            font-size: 1rem;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
        }
        .link-btn:hover {
            background: #357abd;
            transform: scale(1.05);
        }
        .link-btn i {
            margin-right: 0.5rem;
        }

        /* Image styling */
        .header-image {
            border-radius: 16px;
            margin: 1.5rem auto;
            display: block;
            max-width: 600px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .header-image:hover {
            transform: scale(1.02);
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            font-size: 0.9rem;
            color: #718096;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .main {
                padding: 1.5rem;
                margin: 1rem;
            }
            .title {
                font-size: 2.2rem;
            }
            .header-image {
                max-width: 100%;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Load data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommender logic
def recommend(medicine):
    try:
        medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
        distances = similarity[medicine_index]
        medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        return [medicines.iloc[i[0]].Drug_Name for i in medicines_list]
    except IndexError:
        return []

# Main UI
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">💊 Smart Medicine Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover alternative medications with AI-powered precision</div>', unsafe_allow_html=True)

# Header image
try:
    image = Image.open('images/medicine-image.jpg')
    st.image(image, caption='Explore Alternative Medications', use_column_width=True, output_format='auto', cls='header-image')
except FileNotFoundError:
    st.warning("Header image not found. Please ensure 'medicine-image.jpg' is in the 'images' folder.")

# Search input with icon
col1, col2 = st.columns([3, 1])
with col1:
    selected_medicine_name = st.selectbox(
        '🔍 Search for a medicine to find alternatives',
        medicines['Drug_Name'].values,
        help="Select a medicine from the dropdown",
        format_func=lambda x: x.title()
    )
with col2:
    recommend_button = st.button("🔎 Find Alternatives", use_container_width=True)

# Recommendations display
if recommend_button:
    with st.spinner("Analyzing alternatives..."):
        recommendations = recommend(selected_medicine_name)
    if recommendations:
        st.markdown("### Recommended Alternatives")
        for idx, med in enumerate(recommendations, start=1):
            st.markdown(f"""
                <div class="card">
                    <h4>{idx}. {med.title()}</h4>
                    <p>Explore this alternative medicine for similar therapeutic effects.</p>
                    <a class="link-btn" href="https://pharmeasy.in/search/all?name={med}" target="_blank">
                        <i>🛒</i> Buy on PharmEasy
                    </a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("No recommendations found. Please check the medicine name or try another.")

# Footer
st.markdown("""
    <div class="footer">
        Powered by xAI · Built for Healthcare Innovation · © 2025
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
