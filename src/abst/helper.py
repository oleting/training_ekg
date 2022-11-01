
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import use
from numpy import arange
from numpy import ndarray

import yaml

use('Qt5Agg')

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100) -> None:
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def load_yaml():
    yaml_file = open("./data/data_from_teacher.yaml", "r")
    yaml_content = yaml.safe_load(yaml_file)
    return yaml_content

# systole; diastole; puls; af; etco2; spo2, energie, ekg, patches, schockbar


def get_data_from_key(searched_key: str):
    content = load_yaml()
    for key, value in content.items():
        if searched_key == key:
            return value
    return None


def set_data_by_key(wanted_key: str, value) -> None:
    content = load_yaml()
    content[wanted_key] = value
    with open("./data/data_from_teacher.yaml", "w") as f:
        yaml.dump(content, f)
