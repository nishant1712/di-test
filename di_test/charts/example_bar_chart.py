from efficieno.chartsv2 import BarChart
from random import randrange
from .data_bar_chart import data1, data2


class NormalBarChart(BarChart):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        self.add_yaxis("商家A", data1)
        self.add_yaxis("商家B", data2)
        self.set_global_opts(title_opts={
            "show": True,
            "text": "Bar-\u57fa\u672c\u793a\u4f8b",
            "target": "blank",
            "subtext": "\u6211\u662f\u526f\u6807\u9898",
            "subtarget": "blank",
            "padding": 5,
            "itemGap": 10,
            "textAlign": "auto",
            "textVerticalAlign": "auto",
            "triggerEvent": False
        })


