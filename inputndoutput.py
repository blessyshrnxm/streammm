import streamlit as st
import streamlit.components.v1 as components
st.title("🎈 Floating Balloons Demo")
st.write("Click the button to see balloons!")

if st.button("Release Balloons 🎉"):
    st.balloons()
st.text("Plain text here")