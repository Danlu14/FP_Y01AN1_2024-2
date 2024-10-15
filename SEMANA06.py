import streamlit as st

#titulo de la aplicación
st.title("Ejercicios con bucles básicos de python")

#Ejercicio 1: Imprimir 10 veces hola mundo
st.subheader("Ejercicio 1: imprimir 'Hola Mundo'10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range (10):
        st.write ("Hola Mundo")
