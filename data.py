import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Name":['Alice','Bob','Charlie','Dave'],
    'Age':[22,25,26,27],
    'City':['New York','San Francisco','Los Angeles','Los Angeles'],

})

st.write(df)