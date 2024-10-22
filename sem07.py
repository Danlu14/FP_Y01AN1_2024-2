import streamlit as st

def mostrar_menu():
    st.title("Ejemplo de menu")
    st.write("Selecciona una opcion del menu")

    menu = ["Archivo", "Editar", "Ver", "Salir"]
    seleccion = ""

    seleccion =st.radio("Menú", menu)

    if seleccion == "Archivo":
            st.write("Seleccionaste: Archivo")
    elif seleccion == "Editar":
            st.write("Seleccionaste: Editar")
    elif seleccion == "Ver":
            st.write("Seleccionaste: Ver")
    elif seleccion == "Salir":
            st.write("Saliendo del menú")  


if__name__ == "__main__":
    mostrar_menu()