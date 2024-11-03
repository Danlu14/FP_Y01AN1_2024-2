import streamlit as st

# Título de la aplicación
st.title("Calcular el Número Mayor de una Lista de N Números")

# Solicitar al usuario el número de entradas
n = st.number_input("Ingrese la cantidad de números (N):", min_value=1, step=1)

# Inicializar variables
numero_mayor = None  # Acumulador para el número mayor
contador = 0  # Contador de números ingresados

# Recoger los números del usuario
for i in range(n):
    numero = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}")  # key para cada entrada
    contador += 1  # Incrementar el contador
    # Si es el primer número o el número ingresado es mayor que el número mayor actual
    if numero_mayor is None or numero > numero_mayor:
        numero_mayor = numero  # Actualizar el número mayor

# Mostrar el resultado
if contador > 0:  # Verifica que se hayan ingresado números
    st.write(f"El número mayor de la lista es: {numero_mayor}")
else:
    st.write("No se han ingresado números.")
