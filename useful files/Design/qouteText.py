import streamlit as st

styl = """"
<style>
    .CommentPie > p {
        font-family: 'Open Sans', sans-serif;
        font-style: italic;
        font-weight: 400;
        font-size: 25px;
        color: #000;
        line-height: 1.5;
        text-align: left;
    }
    @media (min-width: 498px) and (max-width: 1200px) {
        .CommentPie > p {
            font-size: 20px;
            line-height: 20px;
        }
    }
    @media (max-width: 498px) {
        .CommentPie > p {
            font-size: 16px;
            line-height: 16px;
        }
    }
</style>
"""


def call_qoute(name):
    st.markdown(f"""
    <div class ="Row M-Padding">
    <svg width="87" height="64" viewBox="0 0 87 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path id="Vector" d="M86.9 46C85.9 34.5 75.8 26 64.3 27C66.2 24.1 68.8 21.4 71.8 19.2999C75.1 16.9 78.9 15.2 83.1 14.2L83 12.9C76.7 13.1 64.2 16.9999 56.8 23.0999C53.6 25.6999 51 28.7999 49.1 32.0999C44.8 22.5999 34.8 16.4 23.8 17.2999C26.2 13.6999 29.3 10.5 32.9 7.89995C36.9 4.99995 41.6 2.89995 46.7 1.69995L46.6 0.199951C39 0.399951 23.8 5.19995 14.7 12.6C5.4 20.1 0.5 31 0.5 41.7V41.7999C0.5 42.7999 0.5 43.7999 0.6 44.7999C0.6 44.7999 0.6 44.8 0.6 44.9C1.3 52.6 5.3 59.1 11.2 63.3H40.8C43.3 61.5 45.4 59.2999 47.2 56.6999C48.4 59.1999 50.1 61.4 52.1 63.3H80.2C84.8 59.1 87.5 52.7999 86.9 46Z" fill="url(#paint0_linear_10_433)"/>
        <defs>
        <linearGradient id="paint0_linear_10_433" x1="0.510804" y1="31.7335" x2="87.0074" y2="31.7335" gradientUnits="userSpaceOnUse">
        <stop stop-color="#73265E"/>
        <stop offset="0.1255" stop-color="#7E255E"/>
        <stop offset="0.3486" stop-color="#9D235C"/>
        <stop offset="0.6415" stop-color="#CE205A"/>
        <stop offset="0.7741" stop-color="#E61E59"/>
        <stop offset="0.8894" stop-color="#E12738"/>
        <stop offset="1" stop-color="#DC3115"/>
        </linearGradient>
        </defs>
    </svg>
    </div>
    <div class ="Row CommentPie">
        <p class= "L-Padding" >{name}
        </p>
    </div>""", unsafe_allow_html=True)
    return True
