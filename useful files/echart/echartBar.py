import streamlit_echarts as st_echarts
# echarts bar plot that can be used for both vertical and horizontal plots
# responsive for mobile view


def echart_barplot(variable_list, data, height, key, overflow, max, split, rotation=0, horizontal=True):

    if horizontal == True:  # horizontal bar plot
        options = {
            "yAxis": {
                "type": 'category',
                "data": variable_list,
                "axisTick": {"alignWithLabel": "true"},
                "axisLabel": {
                    "margin": 10,
                    "rotate": rotation,
                    "overflow": overflow,
                    "align": "right"
                }
            },
            "xAxis": {
                "type": 'value',
                "max": max,
                "maxInterval": split,
                "axisLabel": {
                    "formatter": "{value} %",
                }
            },
            "tooltip": {
                "trigger": 'axis',
                "axisPointer": {"type": 'shadow'},
                "formatter": "<b>{b}</b><br />{c}%",
                "confine": "true",
                "extraCssText": 'width:auto; white-space:pre-wrap;',
                "position": 'inside'
            },
            "series": [
                {
                    "data": list(reversed(data)),
                    "type": 'bar',
                    "label": {
                        "show": "true",
                        "position": 'right',
                        "formatter": "{c}%"
                    },
                    "encode": {"x": 'value', "y": 'sector'},
                    "barWidth": '70%',
                    "width": "100%",
                    "height": "100%"
                }
            ],
            "media": [
                {
                    "query": {
                        "minWidth": 400
                    },
                    "option": {
                        "yAxis": {
                            "axisLabel": {
                                "fontSize": 14,
                                "width": 220
                            }
                        },
                        "xAxis": {
                            "axisLabel": {
                                "fontSize": 14,
                            }
                        },
                        "grid": {"left": 230, "top": 10, "right": 50, "bottom": 25},
                        "series": [{
                            "label": {
                                "fontSize": 13
                            }
                        }]
                    }
                },
                {
                    "option": {
                        "yAxis": {
                            "axisLabel": {
                                "fontSize": 11,
                                "width": 110
                            }
                        },
                        "xAxis": {
                            "axisLabel": {
                                "fontSize": 11,
                            }
                        },
                        "grid": {"left": 120, "top": 10, "right": 50, "bottom": 25},
                        "series": [{
                            "label": {
                                "fontSize": 11
                            }
                        }]
                    }
                }
            ]
        }
        figure = st_echarts(options, height=height, width="100%", key=key)
    else:  # vertical bar plot
        options = {
            "xAxis": {
                "type": 'category',
                "data": variable_list,
                "axisTick": {"alignWithLabel": "true"},
                "axisLabel": {
                    "rotate": rotation,
                    "margin": 10,
                    "width": 130,
                    "overflow": overflow,
                    "align": "right"}
            },
            "yAxis": {
                "type": 'value',
                "max": max,
                "maxInterval": split,
                "axisLabel": {
                    "formatter": "{value} %",
                }
            },
            "tooltip": {
                "trigger": 'axis',
                "axisPointer": {"type": 'shadow'},
                "formatter": "<b>{b}</b><br />{c}%",
                "confine": "true",
                "extraCssText": 'width:auto; white-space:pre-wrap;',
                "position": 'inside'
            },
            "series": [
                {
                    "data": data,
                    "type": 'bar',
                    "encode": {"x": 'value', "y": 'sector'},
                    "barWidth": '70%',
                    "width": "100%"
                }
            ],
            "media": [
                {
                    "query": {
                        "minWidth": 400
                    },
                    "option": {
                        "yAxis": {
                            "axisLabel": {
                                "fontSize": 14,
                            }
                        },
                        "xAxis": {
                            "axisLabel": {
                                "fontSize": 14,
                            }
                        },
                        "grid": {"left": 50, "top": 40, "right": 40, "bottom": 80}
                    }
                },
                {
                    "option": {
                        "yAxis": {
                            "axisLabel": {
                                "fontSize": 11,
                            }
                        },
                        "xAxis": {
                            "axisLabel": {
                                "fontSize": 11,
                            }
                        },
                        "grid": {"left": 40, "top": 40, "right": 0, "bottom": 80}
                    }
                }
            ]
        }
        figure = st_echarts(options, height=height,
                            width="100%", key=key)
    return figure
