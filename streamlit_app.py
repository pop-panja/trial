import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My first app")

st.header("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20,3O, columns=("a","b","c")))
st.area_chart(chart_data)
