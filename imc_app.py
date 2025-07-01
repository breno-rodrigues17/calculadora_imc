import streamlit as st
import pandas as pd

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso 🟡"
    elif imc < 24.9:
        return "Peso Normal 🟢"
    elif imc < 29.9:
        return "Sobrepeso 🟠"
    elif imc < 34.9:
        return "Obesidade grau 1 🔴"
    elif imc < 39.9:
        return "Obesidade grau 2 🔴"
    else:
        return "Obesidade grau 3 🔴"

st.title("💪 Calculadora de IMC")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, step=1)
peso = st.number_input("Digite seu peso (kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Digite sua altura (m):", min_value=0.0, format="%.2f")

if "historico" not in st.session_state:
    st.session_state.historico = []

if st.button("📊 Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = calcular_imc(peso, altura)
        categoria = classificar_imc(imc)

        st.success(f"{nome}, seu IMC é: {imc:.2f}")
        st.info(f"Classificação: {categoria}")

        st.session_state.historico.append({
            "Nome": nome,
            "Idade": idade,
            "Peso (kg)": peso,
            "Altura (m)": altura,
            "IMC": round(imc, 2),
            "Classificação": categoria
        })
    else:
        st.warning("⚠️ Preencha todos os campos corretamente.")

# Histórico
if st.session_state.historico:
    st.subheader("📅 Histórico de IMC")
    df = pd.DataFrame(st.session_state.historico)
    st.dataframe(df)


