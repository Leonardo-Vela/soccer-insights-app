import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

st.write("The following is the derivation of results: Assume that there are n events and exactly one of these events will occur. Let ")
st.latex(r'''
    (q_1, \cdots, q_n) \in [1,\infty)^n
    ''')
st.write("be the vector of betting odds.") 