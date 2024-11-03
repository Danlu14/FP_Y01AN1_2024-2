import streamlit as st

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

st.title("Ejercicio5: Calcular el Número Mayor de una Lista de N Números")

numero = st.number_input("Ingrese un número:", step=1.0)

# Botón para agregar el número a la lista
if st.button("Agregar número"):
    st.session_state.numeros.append(numero)
    st.success(f"Número {numero} agregado a la lista.")

# Mostrar la lista de números ingresados
if st.session_state.numeros:
    st.write("Números ingresados:")
    st.write(st.session_state.numeros)

    # Calcular el número mayor
    numero_mayor = max(st.session_state.numeros)
    st.write(f"El número mayor de la lista es: {numero_mayor}")
else:
    st.write("Aún no se ha ingresado ningún número.")

