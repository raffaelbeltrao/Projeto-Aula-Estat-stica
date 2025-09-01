import streamlit as st
from functions.plot_ts import plot


st.title("Histórico de cotações.")
st.write("Veja o histórico das cotações.")
Ticker = st.sidebar.text_input("Ticker da empresa")


if Ticker:
    fig = plot(Ticker)
    st.plotly_chart(fig)