import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# Custom CSS to set background color to white
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;  /* White background */
        color: #000000;            /* Black text for better contrast */
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #f0f0f0; /* Light gray input fields */
        color: #000000;            /* Black text in input fields */
    }
    .stButton>button {
        background-color: #dddddd; /* Light gray buttons */
        color: #000000;            /* Black text on buttons */
    }
    .stAlert {
        background-color: #eeeeee; /* Light gray alerts */
        color: #000000;           /* Black text in alerts */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load saved models
working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(r'C:\Users\hp\Desktop\Disease outbreaks\training_modes\saved\diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(r'C:\Users\hp\Desktop\Disease outbreaks\training_modes\saved\heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(r'C:\Users\hp\Desktop\Disease outbreaks\training_modes\saved\parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreaks System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        glucose = st.text_input('Glucose Level')
    with col3:
        blood_pressure = st.text_input('Blood Pressure value')
    with col1:
        skin_thickness = st.text_input('Skin Thickness value')
    with col2:
        insulin = st.text_input('Insulin Level')
    with col3:
        bmi = st.text_input('BMI value')
    with col1:
        diabetes_pedigree = st.text_input('Diabetes Pedigree Function value')
    with col2:
        age = st.text_input('Age of the Person')

    # Prediction logic
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(pregnancies), float(glucose), float(blood_pressure),
                          float(skin_thickness), float(insulin), float(bmi),
                          float(diabetes_pedigree), float(age)]
            prediction = diabetes_model.predict([user_input])
            diagnosis = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
            st.success(diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = male; 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain types (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Prediction logic
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol),
                          float(fbs), float(restecg), float(thalach), float(exang),
                          float(oldpeak), float(slope), float(ca), float(thal)]
            prediction = heart_disease_model.predict([user_input])
            diagnosis = 'The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        apq = st.text_input('MDVP:APQ')
    with col4:
        dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')

    # Prediction logic
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                          float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                          float(apq3), float(apq5), float(apq), float(dda), float(nhr), float(hnr),
                          float(rpde), float(dfa), float(spread1), float(spread2), float(d2), float(ppe)]
            prediction = parkinsons_model.predict([user_input])
            diagnosis = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
