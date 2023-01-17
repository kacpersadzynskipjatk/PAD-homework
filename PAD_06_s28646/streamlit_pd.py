import time

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

tab1, tab2 = st.tabs(["Ankieta", "Staty"])

with tab1:
    st.header("Ankieta")
    imie = st.text_input('Wpisz imie')
    zapisz_button = st.button("Zapisz", 1)
    if zapisz_button and len(imie) > 0:
        result = f'Imie {imie} zapisane'
        st.success(result)
    elif zapisz_button:
        result = 'Wpisz imie'
        st.error(result)
    nazwisko = st.text_input('Wpisz nazwisko')
    zapisz_button2 = st.button("Zapisz", 2)
    if zapisz_button2 and len(nazwisko) > 0:
        result = f'Imie {nazwisko} zapisane'
        st.success(result)
    elif zapisz_button2:
        result = 'Wpisz nazwisko'
        st.error(result)

with tab2:
    st.header("Staty")
    # uploading data
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        df = pd.read_csv(data)
        with st.spinner('Wait for it...'):
            time.sleep(2)
            st.dataframe(df.head(10))
        st.success('Done!')
        plot_button1 = st.button("wykres 1")
        plot_button2 = st.button("wykres 2")
        if plot_button1:
            # creating a sample array
            a = df[df.columns[1]]
            # specifying the figure to plot
            fig, x = plt.subplots()
            x.hist(a, bins=10)
            # plotting the figure
            st.pyplot(fig)
        if plot_button2:
            # creating a sample array
            a = df[df.columns[2]]
            # specifying the figure to plot
            fig, x = plt.subplots()
            x.hist(a, bins=10)
            # plotting the figure
            st.pyplot(fig)
