🛳️ Titanic Survival Prediction Project
This project covers the complete workflow of building a machine learning model to predict Titanic passenger survival — from data cleaning and exploration, model training, to deploying a Streamlit web app for interactive prediction.
📚 Project Overview
Loaded and explored the Titanic dataset

Cleaned and preprocessed data for ML modeling

Trained a classification model (saved as titanic_model.pkl)

Built a Streamlit app (app.py) for user-friendly survival prediction

Prepared deployment-ready files including requirements.txt and README.md

🗂️ Project Files
titanic-project/
├── app.py # Streamlit application
├── titanic_model.pkl # Trained ML model
├── data.csv # Original Titanic dataset (if included)
├── requirements.txt # Python dependencies
└── README.md # This documentation file
🚀 How to Run the Project Locally
Clone or download the repository to your local machine.

Open your terminal or command prompt and navigate to the project directory:
cd path/to/titanic-project

(Optional but recommended) Create and activate a virtual environment:
python -m venv venv
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

Install the required Python packages:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

The app will open in your browser at http://localhost:8501, where you can input passenger details and get survival predictions.

🧠 Model Inputs
The model takes these inputs:

Passenger Class (Pclass): 1, 2, or 3

Sex: male or female

Age: passenger’s age

Number of siblings/spouses aboard (SibSp)

Number of parents/children aboard (Parch)

Fare paid

Port of Embarkation (S, C, or Q)

🎯 Prediction Output
🎉 Passenger predicted to survive

☹️ Passenger predicted not to survive

📦 Dependencies
Python 3.8+

streamlit

pandas

scikit-learn

joblib
All dependencies are listed in requirements.txt.

🌐 Deployment
You can deploy your Streamlit app to cloud platforms like:

Streamlit Cloud (https://streamlit.io/cloud)

Heroku

AWS Elastic Beanstalk
Just push your project to GitHub and link it to your deployment platform. Make sure requirements.txt and titanic_model.pkl are included in the repo.

🙋‍♂️ Author
AURANG ZAIB
Email: aurangzaibbrcl@gmail.com
Data Science & AI SMIT


📄 License
This project is for educational and demonstration purposes.

