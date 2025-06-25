import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinson_model.sav', 'rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
    #diabetes prediction page
if(selected=='Diabetes Prediction'):
        
        #page title
    st.title('Diabetes Prediction using Machine Learning')
        
        #getting the input data from the user
    col1,col2=st.columns(2)
        
    with col1:
        Pregnancies=st.number_input('Number Of Pregnancies')
            
    with col2:
        Glucose = st.number_input('Glucose Level')
            
    with col1:
        BloodPressure = st.number_input('Blood Pressure Level')
            
    with col2:
        SkinThickness = st.number_input('Skin Thickness Level')
        
    with col1:
        Insulin = st.number_input('Insulin Level')
            
    with col2:
        BMI = st.number_input('BMI Value')
            
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value')
            
    with col2:
        Age = st.number_input('Age of Person')
            
        diab_diagnosis=''
        
        if st.button('Diabetes test result'):
            diab_prediction=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if(diab_prediction[0]==1):
                diab_diagnosis= 'the person is diabetic'
            else:
                diab_diagnosis= 'the person is not diabetic'
        st.success(diab_diagnosis)
        

#heart disease prediction page
if(selected=='Heart Disease Prediction'):
    
    st.title('❤ Heart Disease Prediction using Machine Learning')
    
    col1,col2=st.columns(2)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col1:
        cp = st.text_input('Chest Pain Type (0–3)')  
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Serum Cholestoral (mg/dl)')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)')
    with col1:
        restecg = st.text_input('Resting ECG results (0–2)')
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col2:
        ca = st.text_input('Number of major vessels (0–3)')
    with col1:
        thal = st.text_input('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)')
    
    heart_diagnosis=''
    
    if st.button('Heart Disease Prediction Result'):
        heart_prediction = heart_disease.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                                                    float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                                                    float(ca), float(thal)]])
        
        if(heart_prediction[0] == 0):
            heart_diagnosis = 'You have a healthy heart!'
        else:
            heart_diagnosis = 'You may have a heart disease.'

    st.success(heart_diagnosis)
        
        
if(selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Disease Prediction using Machine Learning')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        name = st.text_input('Name')  # not used for prediction

    with col2:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col3:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col4:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col4:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col1:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col3:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col4:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col1:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col2:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col3:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col4:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col1:
        spread2 = st.text_input('spread2')
    with col2:
        D2 = st.text_input('D2')
    with col3:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[float(name),
            float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
            float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP),
            float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer),
            float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
            float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR),
            float(RPDE), float(DFA), float(spread1), float(spread2),
            float(D2), float(PPE)
        ]])

        if (parkinsons_prediction[0] == 0):
            parkinsons_diagnosis = 'Parkinson’s not detected.'
        else:
            parkinsons_diagnosis = 'Parkinson’s detected.'

    st.success(parkinsons_diagnosis)
