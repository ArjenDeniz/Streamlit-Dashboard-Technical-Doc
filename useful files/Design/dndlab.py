import streamlit as st

styl = """
<style>
    .Dnd {
        text-decoration : none;
        color: #000;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
    }
</style>
"""


def made_in():
    st.markdown("""
    <div class ="Row NoBottom">
        <p> Developed by <a class = "Dnd" href = "https://dndlab.co">dndlab.</a></p>
    </div>
    """, unsafe_allow_html=True)
