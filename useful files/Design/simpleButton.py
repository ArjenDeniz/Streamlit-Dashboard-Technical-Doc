import streamlit as st
styl = """
<style>
    .button {
        display: flex;
        overflow: hidden;
        width:50%;
        margin: 10px;
        padding: 12px 12px;
        cursor: pointer;
        user-select: none;
        transition: all 150ms linear;
        white-space: nowrap;
        text-transform: capitalize;
        background: #fff;
        border: 0 none;
        border-radius: 36px;
        -webkit-appearance: none;
        -moz-appearance:    none;
        appearance:         none;
        justify-content: center;
        align-items: center;
        flex: 0 0 160px;
    }
    .button:hover{
        transition: all 150ms linear;
        opacity: .85;
    }
    .button > p {
        font-family: 'Open Sans', sans-serif;
        font-weight: 500;
        font-size: 15px;
        display:flex;
        margin-bottom: 0;
    }
</style>
"""

st.markdown("""
    <div class = "Centered Row">
    <button class = "button Centered" markdown = 1>

    [Return To Website](https://esem.sosyalgirisimcilikagi.org)

    </button>
    </div>
    """, unsafe_allow_html=True)
