import streamlit as st

st.title("Ejercicio 1: Primeros 10 Números")

# Algoritmo para imprimir los primeros 10 números
st.write("Los primeros 10 números son:")
for i in range(1, 11):
    st.write(i)