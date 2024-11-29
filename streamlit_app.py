import streamlit as st
import math

st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm): ",0)
t = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
    v = math.pi*(r**2)*t
    st.success(f"Volume tabungadalah {v:.2+}")
