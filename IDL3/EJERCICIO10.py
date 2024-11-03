import streamlit as st
import math  # PI

st.title("Ejercicio 10: Cálculo del Área y Perímetro de una Circunferencia")

# Función para calcular el área del círculo
def calcular_area(radio):
    return math.pi * (radio ** 2)

# Función para calcular el perímetro del círculo
def calcular_perimetro(radio):
    return 2 * math.pi * radio


# Solicitar el radio al usuario
radio = st.number_input("Ingrese el radio de la circunferencia:", min_value=0.0, step=0.1)

# Verificar que se haya ingresado un radio positivo
if radio > 0:
    # Calcular área y perímetro
    area = calcular_area(radio)
    perimetro = calcular_perimetro(radio)

    # Mostrar los resultados
    st.write(f"Área de la circunferencia: {area:.2f}")
    st.write(f"Perímetro de la circunferencia: {perimetro:.2f}")
else:
    st.write("Por favor, ingrese un radio válido mayor que 0.")
