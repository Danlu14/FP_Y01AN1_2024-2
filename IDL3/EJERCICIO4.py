import streamlit as st

st.title("Ejercicio 4")

# Inicializar listas y contadores
numeros = []
contador_mayores = 0
contador_iguales = 0
contador_menores = 0

# Ingresar los números
for i in range(10):
    numero = st.number_input(f"Ingrese el número {i + 1}:", min_value=0)  
    numeros.append(numero)

# Calcular la media
media = sum(numeros) / len(numeros) if len(numeros) > 0 else 0

# Contar cuántos son mayores, iguales y menores que 10
for numero in numeros:
    if numero > 10:
        contador_mayores += 1
    elif numero == 10:
        contador_iguales += 1
    else:
        contador_menores += 1

# Mostrar resultados
st.write(f"La media de los números ingresados es: {media}")
st.write(f"Números mayores que 10: {contador_mayores}")
st.write(f"Números iguales a 10: {contador_iguales}")
st.write(f"Números menores que 10: {contador_menores}")
