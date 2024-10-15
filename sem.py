import streamlit as st

# Ejercicio 1: Imprimir 10 veces "Hola mundo"
st.subheader("Ejercicio 1: imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")

#EJERCICIO 4: CALCULAR LA MEDIA Y COMPARAR CON 10
st.subheader("Ejercicio 4: Comparar 10 números con el valor 10")
numeros_ej1 = st.text_input("Ingresa 10 numeros separados por comas:", "12, 7, 15, 10, 20, 25, 30, 8, 7, 6")

if st.button("Ejecutar ejercicio 4"):
    #Convertir la cadena de entrada a una lista de números
    lista_numeros = [int(num) for num in numeros_ej1.split(",")]
    media = sum(lista_numeros) / len(lista_numeros)
    mayores = len ([num for num in lista_numeros if num > 10])
    iguales = en ([num for num in lista_numeros if num == 10])
    menores = en ([num for num in lista_numeros if num < 10])

    st.write (f"la medida es: {media}")
    st.write (f"Mayores que 10: {mayores}")
    st.write (f"Iguales a 10: {iguales}")
    st.write (f"Menores que 10: {menores}")