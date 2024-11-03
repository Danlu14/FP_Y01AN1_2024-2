import streamlit as st

st.title("Ejercicio 9: Array de 10 Números")

# Inicializar el array de 10 posiciones
numeros = [0] * 10  

# Que el usuario ingrese 10 números
st.write("Ingrese 10 números:")

for i in range(10):
    numeros[i] = st.number_input(f"Ingrese el número {i + 1}:", step=1.0)

# Mostrar los valores correspondientes
st.write("Índice y valor de cada posición:")
for i in range(10):
    st.write(f"Índice {i}: Valor {numeros[i]}")

# Calcular la suma total
suma_total = sum(numeros)

# Mostrar la suma total
st.write(f"La suma total de los números ingresados es: {suma_total}")
