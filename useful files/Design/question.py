import streamlit as st

styl = """
<style>
    .GraphQuestion{
        font-size: 26px;
        line-height: 1.5;
        font-family: 'Open Sans', sans-serif;
        font-weight: 700;
        color: #5C2D5B;
        max-width: 900px;
    }
    @media (min-width: 498px) and (max-width: 1200px) {
        .GraphQuestion{
            font-size: 20px;
        }
    }
    @media (min-width: 498px) and (max-width: 1200px) {
        .GraphQuestion{
            font-size: 18px;
        }
    }
</style>
"""

# svg has issues !!!


def call_question(name):
    st.markdown(f"""
    <div class = "M-Margin Centered">
        <svg width="466" height="8" viewBox="0 0 466 8" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path id="Line 5" d="M-2.09867e-06 4.00001L466 3.99997" stroke="#E58E6F" stroke-width="7"/>
        </svg>
        <div class="Row Centered XS-Margin">
            <p class = "GraphQuestion"> {name}</p>
        </div>
        <svg width="466" height="8" viewBox="0 0 466 8" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path id="Line 5" d="M-2.09867e-06 4.00001L466 3.99997" stroke="#E58E6F" stroke-width="7"/>
        </svg>
    </div>""", unsafe_allow_html=True)
    return True
