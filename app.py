import streamlit as st
import pandas as pd
import joblib  # ✅ ADD THIS LINE
import streamlit as st
# load trained model
model=joblib.load('titanic_model.pkl')

st.title("Tiatanic Survival Prediction")

# input features for users to inter data
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ['male', 'female'])
age = st.number_input("Age", min_value=0, max_value=100, value=30)
sibsp = st.number_input("Number of Siblings/Spouses aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children aboard (Parch)", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=500.0, value=32.0)
port = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])

# Convert inputs to model-ready format
sex_num = 1 if sex == 'male' else 0

# Convert Port to numeric (adjust based on your encoding)
port_map = {'S': 0, 'C': 1, 'Q': 2}
port_num = port_map[port]

# Create DataFrame for prediction
input_df = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex_num],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Port': [port_num]
})

if st.button("Predict Survival"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success("🎉 The passenger is predicted to Survive!")
    else:
        st.error("☹️ The passenger is predicted NOT to Survive.")

