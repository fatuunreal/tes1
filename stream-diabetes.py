import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('knn_diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Diabetes Dengan KNN new')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')

with col2:
    Glucose = st.text_input('Input nilai Glucose')

with col1:
    BloodPressure = st.text_input('Input nilai Blood Pressure')

with col2:
    SkinThickness = st.text_input('Input nilai Skin Thickness')

with col1:
    Insulin = st.text_input('Input nilai Insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Input nilai Age')

# Variable untuk hasil prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Validasi input (tidak boleh kosong)
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            diab_diagnosis = 'Semua kolom harus diisi'
        else:
            # Konversi input menjadi float
            diab_prediction = diabetes_model.predict([[
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(Skin
