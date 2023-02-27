import streamlit as st
from Functions.functions import *


def create_page():
    st.markdown("""
    <div class = "Intro">
        <div class="SubChapterTitle" id = "top">
            Environmental Sustainability Report
        </div>
        <div>
            <p class = "IntroComment" style = "color: #632A5D;margin-bottom: 10px;"><span style= "font-weight: 700; color: #632A5D">Lorem ipsum</span> dolor sit amet, 
            consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
            laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
            sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    """, unsafe_allow_html=True)

    comment = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    call_quote(comment)
    made_in()
    return True
