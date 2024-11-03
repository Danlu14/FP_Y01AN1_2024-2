import streamlit as st

st.title("Ejercicio 7: Verificación de Contraseña")

# Inicializar el estado de sesión si no existe
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0

# Solicitar la contraseña
while True:
    contraseña = st.text_input("Ingrese la contraseña:", type="password") 

    if st.button("Verificar"):
        if contraseña == "asdasd":
            st.success("Bienvenido")
            break  
        else:
            st.error("Contraseña incorrecta. Inténtalo de nuevo.")
            st.session_state.intentos += 1  
