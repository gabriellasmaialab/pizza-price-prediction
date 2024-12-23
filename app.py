import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x,y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro: .2f} cm é de {preco_previsto: .2f} reais")

