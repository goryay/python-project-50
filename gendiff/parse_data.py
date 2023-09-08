import json
import yaml
from yaml.loader import SafeLoader
import os


def get_file_data(file):
    _, file_extension = os.path.splitext(file)
    content = open(file, 'r')
    return parse(content, file_extension[1:])


def parse(content, format):
    match format:
        case 'json':
            return json.load(content)
        case 'yml' | 'yaml':
            return yaml.load(content, Loader=SafeLoader)
        case _:
            raise Exception(
                f'Unknown extension: "{format}"! '
                f'I can\'t parse it! '
                f'Use "gendiff -h" to find extensions available'
            )
