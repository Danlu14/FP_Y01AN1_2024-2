import streamlit as st
import numpy as np  

# Título de la aplicación
st.title("Ejercicio 8: Suma y Media de Números del 1 al 100")

numeros = np.arange(1, 101)  

# Calcular la suma y la media
suma = np.sum(numeros)  
media = np.mean(numeros)  

# Mostrar los resultados
st.write(f"Array de números del 1 al 100: {numeros}")
st.write(f"Suma de todos los números: {suma}")
st.write(f"Media de todos los números: {media:.2f}")
