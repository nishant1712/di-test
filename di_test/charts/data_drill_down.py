class ExampleData:

    def __init__(self):
        self.parent_data = {"Animals": 5, "Fruits": 10, "Cars": 10}
        self.child_data = {"Animals": {
            "x_axis": ["cat", "dog", "tiger", "lion"],
            "y_axis": [10, 20, 5, 2]
                        },
            "Fruits": {
                "x_axis": ["apple", "banana", "orange", "mango"],
                "y_axis": [9, 25, 50, 21]
            },
            "Cars": {
                "x_axis": ["sedan", "hatchback", "suv", "muv"],
                "y_axis": [15, 2, 50, 20]
            }
        }

    def get_parent_data(self):
        x_axis_data = list(self.parent_data.keys())
        y_axis_data = [{"value": v, "group_id": k} for k, v in self.parent_data.items()]
        return x_axis_data, y_axis_data

    def get_child_data(self, group_id: str):
        child_data = self.child_data[group_id]
        x_axis_data = child_data["x_axis"]
        y_axis_data = child_data["y_axis"]
        return x_axis_data, y_axis_data
