import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide")

st.title('Stroke Prediction Application')

st.divider()

cols1, cols2, cols3, cols4, cols5 = st.columns(5)

with cols1:
    age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1)
    hypertension = st.selectbox("Hypertension", options=['No', 'Yes'])

with cols2:
    heart_disease = st.selectbox("Heart Disease", options=['No', 'Yes'])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0, max_value=500, value=100, step=1)

# Inputs for categorical variables
with cols3:
    bmi = st.number_input("BMI", min_value=0, max_value=100, value=20, step=1)
    gender = st.selectbox("Gender", options=['Female', 'Male', 'Other'])

with cols4:
    ever_married = st.selectbox("Ever Married", options=['No', 'Yes'])
    work_type = st.selectbox("Work Type", options=['Govt_job', 'Never_worked', 'Private', 'Self-employed', 'children'])

with cols5:
    residence_type = st.selectbox("Residence Type", options=['Rural', 'Urban'])
    smoking_status = st.selectbox("Smoking Status", options=['Unknown', 'formerly smoked', 'never smoked', 'smokes'])

# Mapping for categorical features to numeric
gender_mapping = {'Female': [1, 0, 0], 'Male': [0, 1, 0], 'Other': [0, 0, 1]}
ever_married_mapping = {'No': [1, 0], 'Yes': [0, 1]}
work_type_mapping = {'Govt_job': [1, 0, 0, 0, 0], 'Never_worked': [0, 1, 0, 0, 0], 
                     'Private': [0, 0, 1, 0, 0], 'Self-employed': [0, 0, 0, 1, 0], 
                     'children': [0, 0, 0, 0, 1]}
residence_type_mapping = {'Rural': [1, 0], 'Urban': [0, 1]}
smoking_status_mapping = {'Unknown': [1, 0, 0, 0], 'formerly smoked': [0, 1, 0, 0], 
                          'never smoked': [0, 0, 1, 0], 'smokes': [0, 0, 0, 1]}

# Convert Yes/No to 1/0 for binary categories
hypertension_value = 1 if hypertension == 'Yes' else 0
heart_disease_value = 1 if heart_disease == 'Yes' else 0

# Construct data dictionary with numeric values
data = {
    'age': age,
    'hypertension': hypertension_value,
    'heart_disease': heart_disease_value,
    'avg_glucose_level': avg_glucose_level,
    'bmi': bmi,
    **dict(zip(['gender_Female', 'gender_Male', 'gender_Other'], gender_mapping[gender])),
    **dict(zip(['ever_married_No', 'ever_married_Yes'], ever_married_mapping[ever_married])),
    **dict(zip(['work_type_Govt_job', 'work_type_Never_worked', 'work_type_Private', 
                'work_type_Self-employed', 'work_type_children'], work_type_mapping[work_type])),
    **dict(zip(['Residence_type_Rural', 'Residence_type_Urban'], residence_type_mapping[residence_type])),
    **dict(zip(['smoking_status_Unknown', 'smoking_status_formerly smoked', 
                'smoking_status_never smoked', 'smoking_status_smokes'], smoking_status_mapping[smoking_status])),
}

# Convert to DataFrame
input_df = pd.DataFrame([data])

# Load the trained model
model = pickle.load(open('rf.sav', 'rb'))

st.write("")
if st.button('Predict Stroke'):
  
    predictions = model.predict(input_df)
    if predictions[0] == 1:
        st.write('Stroke Predicti