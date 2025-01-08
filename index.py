import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open(
    "diabetes_model.sav", 'rb'))

heart_model = pickle.load(open(
    "heart_model.sav", 'rb'))

# sidebar

with st.sidebar:
    selector = option_menu('Multiple Disease Predictive System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)


#-------------------------------------------------

# Diabetes Prediction Page
if selector == 'Diabetes Prediction':

    # page title
    st.title("Diabetes Prediction using ML")

    Pregnancies = st.text_input("Number of Pregnancies") 
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age of the Person")

    # code for prediction
    dia_diagnosis = ''
    
    # creating a button
    if st.button("Diabetes Test Result"):
        dia_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if dia_prediction[0] == 1:
            dia_diagnosis = 'The person is diabetic'
        else:
            dia_diagnosis = 'The person is not diabetic'

        st.success(dia_diagnosis)

#------------------------------------------------

# Heart Disease Page
if selector == 'Heart Disease Prediction':

    # page title
    st.title("Heart Disease Prediction using ML")
        
    age = st.text_input('Age')
    sex = st.text_input('Sex')   
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
        