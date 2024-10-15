import streamlit as st

# Ejercicio 1: Imprimir 10 veces "Hola mundo"
st.subheader("Ejercicio 1: imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")