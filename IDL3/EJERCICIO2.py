import streamlit as st

x = st.number_input("Ingresa el valor de x:", min_value=0, step=1)

serie = ""
suma = 0
for i in range(1, 101, 2):
    valor = x + i
    # Añadir cada término a la serie 
    serie += f"({x} + {i}) + "
    suma += valor

# Para eliminar el + del final
st.write("Serie:")
st.write(serie[:-3])

# Mostrar el resultado de la suma
st.write(f"El resultado de la suma es: {suma}")
