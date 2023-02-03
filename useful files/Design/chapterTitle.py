import streamlit as st

# CSS
styl = """
<style>
    #pageStart {
        margin-top: 50px;
    }
    .ChapterTitle {
        font-size: 58px;
        font-family: 'Bitter', serif;
        font-weight: 700;
        line-height: 1.5;
        color: #000;
        text-align: left;
    }
    .SubChapterTitle{
        font-size: 44px;
        line-height: 1.5;
        font-family: 'Bitter', serif;
        font-weight: 700;
        color: #000;
    }
    @media (min-width: 498px) and (max-width: 1200px) {
        .ChapterTitle{
            font-size: 45px;
        }
        .SubChapterTitle{
            font-size: 40px;
        }
    }
    @media (max-width: 498px) {
        .ChapterTitle{
            font-size: 30px;
        }
        .SubChapterTitle{
            font-size: 25px;
        }
    }
</style>
"""
# subchapters


def call_subChapter(name):
    st.markdown(f"""<div class="SubChapterTitle L-Margin">
        {name}
    </div>""", unsafe_allow_html=True)
    return True

# chapters


def call_chapterChapter(title, count, allBig=False):
    st.markdown(f"""
    <div id = "pageStart">
        <p class = "ChapterTitle">{count}) {title}</p>
        <div class="Row">
            <svg width="832" height="6" viewBox="0 0 832 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                <line id="Line 9" y1="2.88867" x2="832" y2="2.88867" stroke="#632A5D" stroke-width="5"/>
            </svg>
        </div>
    </div>""", unsafe_allow_html=True)
    return True
