import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), 'mopmodel.sav')
print(model_path)  # Verify the path
Prediksi_model = pickle.load(open(model_path, 'rb'))

#Judul Web
st.title('KLASIFIKASI ELIGIBILTAS PENERIMA MOP')

GRADE = st.text_input('Input Nilai Grade Anda')
LOS = st.text_input('Input berapa Tahun anda sudah bekerja')
EMPLOYEMENT_STATUS =  st.text_input('Input  Status perkerja anda dalam angka, Permanent = 1, Kontrak = 0')
STSP = st.text_input('Apakah anda pernah mendapatakan Surat Teguran atau Surat Peringatan dalam 12 bulan terakhir ? Pernah input = 0, Tidak pernah = 1')
DEMOTION = st.text_input('Apakah anda pernah mengalami demosi jabatan dalam 12 bulan terakhir ? Pernah input = 0, Tidak pernah input = 1')

Predik = ''

if st.button('Prediksi') :
    Prediksi = Prediksi_model.predict([[GRADE, LOS, EMPLOYEMENT_STATUS, STSP, DEMOTION]])
    if(Prediksi[0] == 1):
        Predik = 'ANDA TIDAK ELIGIBLE'
    else :
        Predik = 'SELAMAT ANDA ELIGIBLE'
    st.success(Predik)

