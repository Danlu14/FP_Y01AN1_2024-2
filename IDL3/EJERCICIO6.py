import streamlit as st

# Inicializar variables en el estado de sesión si no existen
if 'suma_numeros' not in st.session_state:
    st.session_state.suma_numeros = 0
if 'contador_numeros' not in st.session_state:
    st.session_state.contador_numeros = 0

st.title("Ejercicio 6: Suma y Media de Números Introducidos")

st.write("Ingrese números para sumar. Haga clic en 'Agregar número' para registrar un número. Introduzca 0 para finalizar.")

# Input para ingresar un número
numero = st.number_input("Ingrese un número:", step=1.0)

# Botón para agregar el número
if st.button("Agregar número"):
    if numero != 0:
        st.session_state.suma_numeros += numero
        st.session_state.contador_numeros += 1
        st.success(f"Número {numero} agregado.")
    else:
        st.write("Proceso finalizado. Mostrando resultados.")

# Mostrar resultados al finalizar
if st.session_state.contador_numeros > 0 and numero == 0:
    media = st.session_state.suma_numeros / st.session_state.contador_numeros
    st.write(f"Suma total de los números: {st.session_state.suma_numeros}")
    st.write(f"Media de los números ingresados: {media:.2f}")
elif numero == 0:
    st.write("No se ha ingresado ningún número.")

