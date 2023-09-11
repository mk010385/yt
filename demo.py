import streamlit as st
st.title("hello streamlit")
st.header("header")
st.subheader("sub header")
st.text("do u like this video")
st.markdown(""" 
# h1 tag
## h2 tag
:moon:
""")
d= {"name":['makhan',"jp"],
    "class":[12,13]}
st.write(d)