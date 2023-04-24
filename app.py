import streamlit as st
import pandas as pd

view = [100, 150, 30]
# view

st.write("# Youtube view")
st.write("## bar_chart")
st.bar_chart(view)

svview = pd.Series(view)
svview