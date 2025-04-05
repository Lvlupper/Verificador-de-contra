import streamlit as st
import re

def verificar_contraseña(Contraseña):
    if len(Contraseña) < 6:
        return 'La clave debe tener al menos 6 dígitos'
    if " " in Contraseña:
        return 'La clave no debe contener espacios vacios,asi de jodido soy jaja'
    if not re.search(r'[A-Z]', Contraseña):
        return 'La clave debe contener al menos una mayúscula'
    if not re.search(r"\d", Contraseña):
        return "La clave debe tener al menos un número"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", Contraseña):
        return "Debe tener al menos un signo, espeso soy jajaj"
    return "¡Felicidades haz creado una contraseña segurísima!"

st.title("🔐 Verificador de Contraseña Segura 100xciento real")

Contraseña = st.text_input("Ingresa tu mejor contraseña:")

if st.button("Verificar clave"):
    resultado = verificar_contraseña(Contraseña)
    st.success(resultado)
