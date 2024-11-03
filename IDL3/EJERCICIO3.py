import streamlit as st

st.tittle("Ejercicio 3: Promedio de pares")

pares = [i for i in range(20, 401, 2)]

# Calcular el promedio
suma_pares = sum(pares)
cantidad_pares = len(pares)
promedio = suma_pares / cantidad_pares

# Mostrar el resultado 
st.write("Los números pares entre 20 y 400 son:")
st.write(pares)
st.write(f"El promedio de estos números pares es: {promedio}")