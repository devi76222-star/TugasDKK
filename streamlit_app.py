import streamlit as st

st.title("penjumlahan")
st.markdown(
    """ 
    Devi Apriliana Saputri 9 
    """
)

import streamlit as st

st.title("Aplikasi Pertambahan")

# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0)
angka2 = st.number_input("Masukkan angka kedua", value=0)

# Tombol hitung
if st.button("Hitung"):
    hasil = angka1 + angka2
    st.success(f"Hasil pertambahan: {hasil}")
if st.button("Send balloons!"):
    st.balloons()

