import yaml
import os


class Get_Yaml:
    def __init__(self):
        pass

    def get_yaml_file(self, yaml_path):
        with open('./Data' + os.sep +yaml_path, 'r', encoding='utf-8')as f:
            return yaml.load(f)
