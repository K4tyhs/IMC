import streamlit as st

st.title("IMC!")
nome = st.text_input("Digite seu nome: ")

peso = st.number_input("Digite o seu peso", min_value=0.1, format="%.2r")
altura = st.number_input("Digite a sua altura", min_value=0.1, format="%.2r")

valor_total = peso / (altura**2)
if st.button("Calcular total"):
    if valor_total <= 18.5:
        st.write(f"Olá, {nome}! O seu IMC é de {valor_total:.2f}kg/m2")
        st.write("IMC = MAGREZA")
    elif valor_total > 18.5 and valor_total <= 24.9:
        st.write(f"Olá, {nome}! O seu IMC é de {valor_total:.2f}kg/m2")
        st.write("IMC = NORMAL")
    elif valor_total >= 25 and valor_total <= 29.9:
        st.write(f"Olá, {nome}! O seu IMC é de {valor_total:.2f}kg/m2")
        st.write("IMC = SOBREPESO")
    elif valor_total >= 30 and valor_total <= 39.9:
        st.write(f"Olá, {nome}! O seu IMC é de {valor_total:.2f}kg/m2")
        st.write("IMC = OBESIDADE")
    elif valor_total >= 40:
        st.write(f"Olá, {nome}! O seu IMC é de {valor_total:.2f}kg/m2")
        st.write("IMC = OBESIDADE GRAVE")
