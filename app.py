import streamlit as st
import pandas as pd

view = [100, 150, 30]
# view

st.write("# Youtube view")
st.write("## bar_chart")
st.bar_chart(view)

svview = pd.Series(view)
svview

from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder()
raw_data_cat_onehot = onehot_encoder.fit_transform(raw_data_cat)
print(raw_data_cat_onehot.toarray()[:10])
print(onehot_encoder.categories_)
