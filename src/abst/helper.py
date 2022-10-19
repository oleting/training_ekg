import yaml


def load_yaml():
    yaml_file = open("./data/data_from_teacher.yaml", "r")
    yaml_content = yaml.safe_load(yaml_file)
    return yaml_content

# systole; diastole; puls; af; etco2; spo2, energie, ekg


def get_data_from_key(searched_key: str):
    content = load_yaml()
    for key, value in content.items():
        if searched_key == key:
            return value
    return NoneType


def set_data_by_key(wanted_key: str, value):
    content = load_yaml()
    content[wanted_key] = value
    with open("./data/data_from_teacher.yaml", "w") as f:
        yaml.dump(content, f)
