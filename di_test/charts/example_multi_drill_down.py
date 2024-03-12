from efficieno.chartsv2 import BarChart
from .data_multi_drill_down import ExampleData


example_dataset = ExampleData()


class GrandChild(BarChart):
    def __init__(self, group_id: str = "Animals.cat", *args, **kwargs):
        x_axis_value, y_axis_value = example_dataset.get_grand_child_data(group_id=group_id)

        super().__init__(*args, **kwargs)
        self.add_xaxis(x_axis_value)
        self.add_yaxis("values", y_axis_value)
        # self.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        self.set_global_opts(
            title_opts={
                "show": True,
                "text": "Bar Chart Child",
                "target": "blank",
                "subtext": "Child Chart  ",
                "subtarget": "blank",
                "padding": 5,
                "itemGap": 10,
                "textAlign": "auto",
                "textVerticalAlign": "auto",
                "triggerEvent": False,
            }
        )


class ChildChart(BarChart):
    child_chart = GrandChild

    def __init__(self, group_id: str = "Animals", *args, **kwargs):
        x_axis_value, y_axis_value = example_dataset.get_child_data(group_id=group_id)

        super().__init__(*args, **kwargs)
        self.add_xaxis(x_axis_value)
        self.add_yaxis("values", y_axis_value)
        # self.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        self.set_global_opts(
            title_opts={
                "show": True,
                "text": "Bar Chart Child",
                "target": "blank",
                "subtext": "Child Chart  ",
                "subtarget": "blank",
                "padding": 5,
                "itemGap": 10,
                "textAlign": "auto",
                "textVerticalAlign": "auto",
                "triggerEvent": False,
            }
        )


class ParentChart(BarChart):
    child_chart = ChildChart

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        x_axis_value, y_axis_value = example_dataset.get_parent_data()
        self.add_xaxis(x_axis_value)
        self.add_yaxis("values", y_axis_value)
        self.set_global_opts(
            title_opts={
                "show": True,
                "text": "Bar Chart Parent",
                "target": "blank",
                "subtext": "parent chart ",
                "subtarget": "blank",
                "padding": 5,
                "itemGap": 10,
                "textAlign": "auto",
                "textVerticalAlign": "auto",
                "triggerEvent": False,
            }
        )
