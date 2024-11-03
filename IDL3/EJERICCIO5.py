import streamlit as st

st.title("EJERCICIO 5: Calcular el Número Mayor de una Lista de N Números")

# Ingresar la cantidad de números
n = st.number_input("Ingrese la cantidad de números (N):", min_value=1, step=1)

# Inicializar la lista
numeros = []

# Recoger los números del usuario
for i in range(n):
    numero = st.number_input(f"Ingrese el número {i + 1}:")
    numeros.append(numero)

# Calcular el número mayor
if numeros:  # Verifica si la lista no está vacía
    numero_mayor = max(numeros)
    st.write(f"El número mayor de la lista es: {numero_mayor}")
else:
    st.write("No se han ingresado números.")