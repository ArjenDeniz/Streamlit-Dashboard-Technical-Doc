import streamlit as st


def create_style(scss=""):
    styl = """
    <meta name = "description" content= "Climate & Energy Report Example">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bitter:wght@400;500;700&family=Open+Sans:ital,wght@0,400;0,500;0,600;0,700;1,300&display=swap" rel="stylesheet">
    <style>
        a{
            text-decoration: none;
        }
        .css-nlntq9 a{ 
            color: inherit !important;
        }
        .XL-Margin{
            margin-top:50px;
            margin-bottom:50px;
        }
        .L-Margin{
            margin-top: 40px;
            margin-bottom: 40px;
        }
        .M-Margin{
            margin-top: 30px;
            margin-bottom: 30px;
        }
        .S-Margin{
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .XS-Margin{
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .B-Margin{
            margin-left: 50px;
        }
        .NoBottom{
            margin-bottom: 0px;
        }
        .L-Padding{
            padding-left: 20px;
            padding-right: 20px;
        }
        .M-Padding {
            padding-left: 10px;
            padding-right: 10px;
        }
        .S-Padding{
            padding-left: 5px;
            padding-right: 5px;
        }
        .Centered{
            text-align: center;
            justify-content:center;
            align-items: center;
            align-self: center;
        }
        .Row{
            display: flex;
        }
        .limited {
            max-width: 1200px;
            margin: auto;
        }
        .column{
            padding: 0 2vw;
            margin: 0 0 .75rem 0;
        }
        .Dnd {
            text-decoration : none;
            color: #000;
            font-family: 'Poppins', sans-serif;
            font-weight: 800;
        }
        .CommentPie > p {
            font-family: 'Open Sans', sans-serif;
            font-style: italic;
            font-weight: 400;
            font-size: 25px;
            color: #000;
            line-height: 1.5;
            text-align: left;
        }
        #pageStart {
            margin-top: 50px;
        }
        .stickyButton{
            border: 2px solid ;
            background-color: #632A5D;
            border-radius: 50px;
            height: 50px;
            width: 50px;
            text-align: center; 
            color: #fff;   
        }
        .Arrow{
            text-decoration: none;
            font-family: 'Bitter', serif;
            font-weight: 400;
            font-size: 40px;
            line-height: 50px;
            color: #fff !important;
        }
        .stickyButton:hover {
            background: #fff;
            color: #632A5D !important;
        }
        .stickyButton:hover .Arrow{
            color: #632A5D !important;
            text-decoration: none !important;
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
        @media (min-width: 498px) and (max-width: 1200px) {
            .CommentPie > p {
                font-size: 20px;
                line-height: 20px;
            }
            .ChapterTitle{
                font-size: 45px;
            }
            .SubChapterTitle{
                font-size: 40px;
            }
        }
        @media (max-width: 498px) {
            .XL-Margin{
                margin-top:25px;
                margin-bottom:25px;
            }
            .L-Margin{
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .M-Margin{
                margin-top: 15px;
                margin-bottom: 15px;
            }
            .S-Margin{
                margin-top: 10px;
                margin-bottom: 10px;
            }
            .XS-Margin{
                margin-top: 5px;
                margin-bottom: 5px;
            }
            .B-Margin{
                margin-left: 20px;
            }
            .L-Padding{
                padding-left: 10px;
                padding-right: 10px;
            }
            .M-Padding {
                padding-left: 5px;
                padding-right: 5px;
            }
            .CommentPie > p {
                font-size: 16px;
                line-height: 16px;
            }
            .ChapterTitle{
                font-size: 30px;
            }
            .SubChapterTitle{
                font-size: 25px;
            }
        }
    </style>
    """
    return styl
