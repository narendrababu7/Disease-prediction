import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide', page_icon="🧑‍⚕️")

# Check if model files exist
model_paths = {
    "diabetes_model": r"C:\Users\hp\Desktop\Disease outbreak1\training model\diabetes_model.sav",
    "heart_model": r"C:\Users\hp\Desktop\Disease outbreak1\training model\heart_model.sav",
    "parkinsons_model": r"C:\Users\hp\Desktop\Disease outbreak1\training model\parkinsons_model.sav"
}

for model_name, path in model_paths.items():
    if not os.path.exists(path):
        st.error(f"File not found: {path}")
    else:
        st.success(f"File found: {path}")

# Load models if files exist
if all(os.path.exists(path) for path in model_paths.values()):
    diabetes_model = pickle.load(open(model_paths["diabetes_model"], 'rb'))
    heart_model = pickle.load(open(model_paths["heart_model"], 'rb'))
    parkinsons_model = pickle.load(open(model_paths["parkinsons_model"], 'rb'))
else:
    st.error("One or more model files are missing. Please check the file paths.")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                          ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                          menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age of the person')
    with col2:
        Sex = st.text_input('Sex of the person')
    with col3:
        cp = st.text_input('Chest Pain Type (cp)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    with col2:
        chol = st.text_input('Serum Cholestoral (chol)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', [0, 1, 2])
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('Depression Induced by Exercise Relative to Rest (oldpeak)')
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment (slope)', [0, 1, 2])
    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy (ca)', [0, 1, 2, 3])
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

# Parkinson’s Prediction
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction Using ML')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    with col1:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col3:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col4:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col1:
        MDVP_Shim = st.text_input('MDVP:Shimmer')
    with col2:
        Shimmer_db = st.text_input('MDVP:Shimmer(db)')
    with col3:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col4:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('spread1')
    with col4:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    Parkinsons_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ,
                      Jitter_DDP, MDVP_Shim, Shimmer_db, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        Parkinsons_prediction = parkinsons_model.predict([user_input])
        if Parkinsons_prediction[0] == 1:
            Parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            Parkinsons_diagnosis = 'The person does not have Parkinsons disease'
    st.success(Parkinsons_diagnosis)