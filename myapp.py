import streamlit as st


st.set_page_config(
    page_title="APP"


)
st.image('OIP.jpg')

footer_html = """<div style='text-align: center;'>
  <p>Developed ❤️ by Guyo </p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)
