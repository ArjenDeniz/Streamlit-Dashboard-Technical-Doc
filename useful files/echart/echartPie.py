import streamlit_echarts as st_echarts
# echarts pie plot
# responsive for mobile view

# hover labels inside the graph for readability


def echart_pieplot(df, colors, key):
    options = {
        "tooltip": {
            "trigger": 'item',
            "position": 'inside',
            "extraCssText": 'width:auto; white-space:pre-wrap;',
        },
        "grid": {"left": 0, "top": 0, "right": 0, "bottom": 0},
        "series": [
            {
                "type": 'pie',
                "radius": '65%',
                "center": ['52%', '50%'],
                "label": {
                        "position": "outside",
                        "formatter": "{b}\n{c}%",
                        "font-family": "'Open Sans', sans-serif",
                        "overflow": "break"
                },
                "labelLine": {
                    "length": 10,
                    "length2": 0
                },
                "data": df,
                "color": colors,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ],
        "media": [{
            "query": {
                "minWidth": 400
            },
            "option": {
                "series": [{
                    "label": {
                        "fontSize": 14,
                        "lineHeight": 15,
                    }}
                ]
            }},
            {
                "option": {
                    "series": [{
                        "label": {
                            "lineHeight": 11,
                            "fontSize": 11,
                        }
                    }]
                }
        }
        ]
    }
    figure = st_echarts(options, height="350px", width="100%", key=key)
    return figure
