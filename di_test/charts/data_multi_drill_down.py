class ExampleData:

    def __init__(self):
        self.parent_data = {"Animals": 5, "Fruits": 10, "Cars": 10}
        self.child_data = {"Animals": {
                            "cat": 10,
                            "dog": 20,
                            "tiger": 5,
                            "lion": 2
        },
            "Fruits": {
                "apple": 9,
                "banana": 25,
                "orange": 50,
                "mango": 21
            },
            "Cars": {
                "sedan": 15,
                "hatchback": 2,
                "suv": 50,
                "muv": 20
            }
        }
        self.grand_child_data = {
            "Animals": {"cat": {"black": 5, "brown": 2, "white": 3},
                        "dog": {"labrador": 5, "shizu": 2, "golden_retriever": 3},
                        "tiger": {"wild": 5, "parks": 2, "zoo": 3},
                        "lion": {"young": 5, "middle": 2, "old": 3}},
            "Fruits": {"apple": {"fresh": 5, "mid_life": 2, "rotten": 3},
                       "banana": {"indian": 5, "us": 2, "africa": 3},
                       "orange": {"nagpur": 5, "mexico": 2, "china": 3},
                       "mango": {"normal": 5, "devgad": 2, "alphanso": 3}},
            "Cars": {"sedan": {"auto": 5, "manual": 2, "mixed": 3},
                     "hatchback": {"medium": 5, "small": 2, "large": 3},
                     "suv": {"semi": 5, "mid": 2, "full": 3},
                     "muv": {"electric": 5, "diesel": 2, "petrol": 3}}
        }

    def get_parent_data(self):
        x_axis_data = list(self.parent_data.keys())
        y_axis_data = [{"value": v, "group_id": k} for k, v in self.parent_data.items()]
        return x_axis_data, y_axis_data

    def get_child_data(self, group_id: str):
        x_axis_data = list(self.child_data[group_id].keys())
        y_axis_data = [{"value": v, "group_id": f"{group_id}.{k}"} for k, v in self.child_data[group_id].items()]
        return x_axis_data, y_axis_data

    def get_grand_child_data(self, group_id: str):
        parent = group_id.split(".")[0]
        child = group_id.split(".")[1]
        grand_child_data_ex = self.grand_child_data[parent][child]

        x_axis_data = list(grand_child_data_ex.keys())
        y_axis_data = [{"value": v, "group_id": f"{group_id}.{k}"} for k, v in grand_child_data_ex.items()]
        return x_axis_data, y_axis_data
