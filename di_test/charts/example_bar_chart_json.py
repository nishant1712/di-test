from efficieno.chartsv2 import BarChart, create_chart_class

chart_data = {
    "chart_name": "demo_chart1",
    "animation": True,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "aria": {"enabled": False},
    "color": ["#5470c6", "#91cc75", "#fac858", "#ee6666", "#73c0de", "#3ba272", "#fc8452", "#9a60b4", "#ea7ccc"],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": True,
            "data": [68, 1, 31, 22, 1, 1],
            "realtimeSort": False,
            "showBackground": False,
            "stackStrategy": "samesign",
            "cursor": "pointer",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": True,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": True,
            "zlevel": 0,
            "z": 2,
            "label": {"show": True, "margin": 8},
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": True,
            "data": [80, 90, 53, 74, 91, 64],
            "realtimeSort": False,
            "showBackground": False,
            "stackStrategy": "samesign",
            "cursor": "pointer",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": False,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": True,
            "zlevel": 0,
            "z": 2,
            "label": {"show": True, "margin": 8},
        },
    ],
    "legend": [
        {
            "data": ["\u5546\u5bb6A", "\u5546\u5bb6B"],
            "selected": {},
            "show": True,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1,
            "borderRadius": 0,
            "pageButtonItemGap": 5,
            "pageButtonPosition": "end",
            "pageFormatter": "{current}/{total}",
            "pageIconColor": "#2f4554",
            "pageIconInactiveColor": "#aaa",
            "pageIconSize": 15,
            "animationDurationUpdate": 800,
            "selector": False,
            "selectorPosition": "auto",
            "selectorItemGap": 7,
            "selectorButtonGap": 10,
        }
    ],
    "tooltip": {
        "show": True,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {"type": "line"},
        "showContent": True,
        "alwaysShowContent": False,
        "showDelay": 0,
        "hideDelay": 100,
        "enterable": False,
        "confine": False,
        "appendToBody": False,
        "transitionDuration": 0.4,
        "textStyle": {"fontSize": 14},
        "borderWidth": 0,
        "padding": 5,
        "order": "seriesAsc",
    },
    "xAxis": [
        {
            "show": True,
            "scale": False,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": False,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": True,
                "lineStyle": {"show": True, "width": 1, "opacity": 1, "curveness": 0, "type": "solid"},
            },
            "data": [
                "\u886c\u886b",
                "\u7f8a\u6bdb\u886b",
                "\u96ea\u7eba\u886b",
                "\u88e4\u5b50",
                "\u9ad8\u8ddf\u978b",
                "\u889c\u5b50",
            ],
        }
    ],
    "yAxis": [
        {
            "show": True,
            "scale": False,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": False,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": True,
                "lineStyle": {"show": True, "width": 1, "opacity": 1, "curveness": 0, "type": "solid"},
            },
        }
    ],
    "title": [
        {
            "show": True,
            "text": "Bar-\u57fa\u672c\u793a\u4f8b",
            "target": "blank",
            "subtext": "\u6211\u662f\u526f\u6807\u9898",
            "subtarget": "blank",
            "padding": 5,
            "itemGap": 10,
            "textAlign": "auto",
            "textVerticalAlign": "auto",
            "triggerEvent": False,
        }
    ],
}


class BarChartWithJsonData(BarChart):

    def __init__(self, *args, **kwargs):
        super().__init__(chart_data)

