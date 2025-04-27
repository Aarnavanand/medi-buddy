### MediBuddy - Smart Medicine Recommender 🏥💊

MediBuddy is an intelligent medicine recommendation system designed to help users discover alternative medications similar to their prescribed or preferred medicines. Leveraging advanced machine learning techniques, MediBuddy analyzes a comprehensive medicine database and provides personalized, accurate recommendations based on similarity metrics.

🚀 Project Overview
  🔍 Smart Recommendations: Get up to 5 alternative medicines based on your selected prescription.
  🎯 Interactive Interface: Sleek, user-friendly UI with intuitive navigation.
  🛒 E-commerce Integration: Direct links to purchase recommended medicines on PharmEasy.
  📱 Responsive Design: Seamless experience across desktop and mobile devices.

🛠️ Tech Stack
  Frontend & Backend: Streamlit (Python Web Framework)
  Machine Learning: Similarity-based recommendation algorithm
  Data Processing: Pandas, Pickle
  UI Design: Custom CSS with a modern turquoise color palette

📦 Getting Started
  Prerequisites
  Python 3.7 or higher
  
  Required Python packages (listed in requirements.txt)
  
📦 Installation
### Clone the Repository

```bash
git clone https://github.com/Aarnavanand/medi-buddy
cd medi-buddy
```
Install Dependencies
```bash
  pip install -r requirements.txt
```

Run the Application
```bash
  streamlit run app.py
```

🧑‍⚕️ How to Use
  Select a medicine name from the dropdown menu.  
  Click the "🔎 Recommend" button.
  View a list of recommended alternative medicines.
  Click "Buy on PharmEasy" to purchase the medicine directly.

Note:
  The application uses a preprocessed dataset (medicine_dict.pkl) and a pre-computed similarity matrix (similarity.pkl). The database includes:
  Medicine Names
  Categories / Usage Reasons

Descriptions

🌟 Future Enhancements
  📄 Add detailed medicine information (dosage, composition, side effects)
  💰 Price comparison across multiple online pharmacies
  👤 User accounts to save preferences and recommendations
  🎛️ Filtering options (e.g., price range, category)
  🩺 Integration with prescription uploads and doctor approvals

📜 License
  This project is licensed under the MIT License – see the LICENSE file for details.

🙏 Acknowledgments
  Medication data sourced from trusted pharmaceutical databases
  UI icons and design inspired by modern healthcare applications
  E-commerce linking powered by PharmEasy

Live on: https://medi-buddy.streamlit.app/

"An AI-powered Smart Medicine Recommender built with Streamlit, helping users find alternative medications with a seamless e-commerce experience."

📜 License
This project is licensed under the MIT License.
