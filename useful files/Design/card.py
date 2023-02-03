import streamlit as st
styl = """
<style>
.Card {
    background-image: url();
    background-size:cover;
    max-height: 800px;
    max-width: 600px;
    border-radius: 30px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease-in-out;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
.Card:hover {
    transform: scale(1.05);
    transition: all 0.2s ease-in-out;
    cursor: pointer;
    box-shadow: inset 0 0 0 1000px rgba(0, 0, 0, .7);
    transition: all 0.2s ease-in-out;
    .HoverDescription{
        visibility: visible;
        opacity: 1;
    }
    .CardTitle, .CardDescription, .HoverDescription{
        color: #fff;
    }
}
.HoverDescription{
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.2s visibility 0.2s;
    padding: 40px;
}
</style>
"""

st.markdown("""
    <section class = "Card">
        <h2 class= "CardTitle">
            <svg width="50" height="25" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 34 2"
                style="enable-background:new 0 0 34 2;" xml:space="preserve">
                <rect x="0" y="0" fill="#"  width="30" height="2" />
            </svg>
            Lorem ipsum
        </h2>
        <a class="Link" href="#">
            <p class="HoverDescription">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                incididunt ut labore et dolore magna
                aliqua. Leo integer malesuada nunc vel risus.</p>
        </a>
    </section>""", unsafe_html_allow=True)
