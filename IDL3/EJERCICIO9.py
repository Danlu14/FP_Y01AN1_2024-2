import streamlit as st
import numpy as np  # Importar numpy para manejar arrays

# Título de la aplicación
st.title("Ejercicio: Array de 10 Números")

# Inicializar el array de 10 posiciones
numeros = np.zeros(10)  # Crear un array de ceros de 10 posiciones

# Pedir al usuario que ingrese 10 números
st.write("Ingrese 10 números:")

for i in range(10):
    numeros[i] = st.number_input(f"Ingrese el número {i + 1}:", step=1.0)

# Mostrar los índices y valores correspondientes
st.write("Índice y valor de cada posición:")
for i in range(10):
    st.write(f"Índice {i}: Valor {numeros[i]}")

# Calcular la suma total
suma_total = np.sum(numeros)

# Mostrar la suma total
st.write(f"La suma total de los números ingresados es: {suma_total}")
