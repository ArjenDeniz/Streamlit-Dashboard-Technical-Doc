from Pages.CSS.generalStyle import create_style
from Pages import chapter1, chapter2, intro
from streamlit_option_menu import option_menu
import streamlit as st

st.set_page_config(page_title="Report Title",
                   page_icon="🌍", layout="wide")


st.markdown(create_style(), unsafe_allow_html=True)
# option menu


# Sidebar Title
st.sidebar.image("images/logo.png",
                 use_column_width=True)
st.sidebar.title("Report Name")
# Sidebar Menu
with st.sidebar:
    selected = option_menu("", ["Introduction", "Chapter 1", "Chapter 2",],
                           icons=["caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill"], styles={
        "container": {"background-color": "#7ba5d3", "border-radius": "0"},
        "nav-link": {"font-size": "15px", "color": "#FFF", "font-family": "'Open Sans', sans-serif", "font-weight": "500", "--hover-color": "#49637e"},
        "nav-link-selected": {"background-color": "#fff", "color": "#7ba5d3"}
    }, default_index=0)

    st.markdown("""
    <div class = "Centered Row">
    <button class = "button Centered" markdown = 1>

    [Return To Website](http://dndlab.co)
    
    </button>
    </div>
    """, unsafe_allow_html=True)

if selected == "Introduction":
    intro.create_page()

if selected == "Chapter 1":
    chapter1.create_page()

if selected == "Chapter 2":
    chapter2.create_page()
