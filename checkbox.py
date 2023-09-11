import streamlit as st
if st.checkbox("You accpt the T&C",value=True):
    st.write("Thanku")
v1=st.radio("color",["r","g","b"],index=1)
v2=st.selectbox("colors",["r","g","b"],index=0)
st.write(v1,v2)