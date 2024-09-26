import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide")

st.title('Stroke Prediction Application')

st.divider()

# Model selection
model_type = st.selectbox("Select Model", options=["Gradient Boosting Classifier", "Logistic Regression"])

# Input fields
cols1, cols2, cols3, cols4, cols5 = st.columns(5)

with cols1:
    age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1)
    hypertension = st.selectbox("Hypertension", options=['No', 'Yes'])

with cols2:
    heart_disease = st.selectbox("Heart Disease", options=['No', 'Yes'])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0, max_value=500, value=100, step=1)

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
# Gender mapping
if gender == 'Female':
    gender_Female = 1
    gender_Male = 0
    gender_Other = 0
elif gender == 'Male':
    gender_Female = 0
    gender_Male = 1
    gender_Other = 0
else:
    gender_Female = 0
    gender_Male = 0
    gender_Other = 1

# Ever married mapping
if ever_married == 'No':
    ever_married_No = 1
    ever_married_Yes = 0
else:
    ever_married_Yes = 1
    ever_married_No = 0

# Work type mapping
if work_type == 'Govt_job':
    work_type_Govt_job = 1
    work_type_Never_worked = 0
    work_type_Private = 0
    work_type_Self_employed = 0
    work_type_children = 0
elif work_type == 'Never_worked':
    work_type_Govt_job = 0
    work_type_Never_worked = 1
    work_type_Private = 0
    work_type_Self_employed = 0
    work_type_children = 0
elif work_type == 'Private':
    work_type_Govt_job = 0
    work_type_Never_worked = 0
    work_type_Private = 1
    work_type_Self_employed = 0
    work_type_children = 0
elif work_type == 'Self-employed':
    work_type_Govt_job = 0
    work_type_Never_worked = 0
    work_type_Private = 0
    work_type_Self_employed = 1
    work_type_children = 0
else:
    work_type_Govt_job = 0
    work_type_Never_worked = 0
    work_type_Private = 0
    work_type_Self_employed = 0
    work_type_children = 1

# Residence type mapping
if residence_type == 'Rural':
    Residence_type_Rural = 1
    Residence_type_Urban = 0
else:
    Residence_type_Rural = 0
    Residence_type_Urban = 1

# Smoking status mapping
if smoking_status == 'Unknown':
    smoking_status_Unknown = 1
    smoking_status_formerly_smoked = 0
    smoking_status_never_smoked = 0
    smoking_status_smokes = 0
elif smoking_status == 'formerly smoked':
    smoking_status_Unknown = 0
    smoking_status_formerly_smoked = 1
    smoking_status_never_smoked = 0
    smoking_status_smokes = 0
elif smoking_status == 'never smoked':
    smoking_status_Unknown = 0
    smoking_status_formerly_smoked = 0
    smoking_status_never_smoked = 1
    smoking_status_smokes = 0
else:
    smoking_status_Unknown = 0
    smoking_status_formerly_smoked = 0
    smoking_status_never_smoked = 0
    smoking_status_smokes = 1

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
    'gender_Female': gender_Female,
    'gender_Male': gender_Male,
    'gender_Other': gender_Other,
    'ever_married_No': ever_married_No,
    'ever_married_Yes': ever_married_Yes,
    'work_type_Govt_job': work_type_Govt_job,
    'work_type_Never_worked': work_type_Never_worked,
    'work_type_Private': work_type_Private,
    'work_type_Self_employed': work_type_Self_employed,
    'work_type_children': work_type_children,
    'Residence_type_Rural': Residence_type_Rural,
    'Residence_type_Urban': Residence_type_Urban,
    'smoking_status_Unknown': smoking_status_Unknown,
    'smoking_status_formerly_smoked': smoking_status_formerly_smoked,
    'smoking_status_never_smoked': smoking_status_never_smoked,
    'smoking_status_smokes': smoking_status_smokes
}

# Convert to DataFrame
input_df = pd.DataFrame([data])
input_df = input_df.iloc[0].tolist()
input_df = [input_df]

# Load the scaler and the trained model
# Load the scaler
with open('scaler.pkl', 'rb') as n:
    scaler = pickle.load(n)  

# Load the appropriate model based on selection
if model_type == "Gradient Boosting Classifier":
    with open('gbc.sav', 'rb') as f:
        model = pickle.load(f)  # Load the GBC model
else:
    with open('reg_model.sav', 'rb') as r:
        model = pickle.load(r)  # Load the Logistic Regression model

## This is to  make sure every feature is in order.
# # print(data)
# print(input_df)
# feature_names = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
#                  'gender_Female', 'gender_Male', 'gender_Other', 'ever_married_No',
#                  'ever_married_Yes', 'work_type_Govt_job', 'work_type_Never_worked',
#                  'work_type_Private', 'work_type_Self-employed', 'work_type_children',
#                  'Residence_type_Rural', 'Residence_type_Urban', 'smoking_status_Unknown',
#                  'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes']
# # Scale the input data
input_scaled = scaler.transform(input_df)
# print(input_scaled)
# scaled_df = pd.DataFrame(input_scaled, columns=feature_names)
# # Print the scaled values along with the corresponding feature names
# print(scaled_df)

st.write("")
if st.button('Predict Stroke Risk'):
    probabilities = model.predict_proba(input_scaled)
    predictions = model.predict(input_scaled)
    
    st.write(f"Predicted probabilities: {probabilities}")
    
    if predictions[0] == 1:
        st.write('Risk of stroke: Positive')
    else:
        st.write('Risk of stroke: Negative')
