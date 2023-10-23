from gendiff.get_diff import get_diff
from gendiff.parse_data import get_value
from gendiff.format.stylish import make_stylish
from gendiff.format.plain import make_plain
from gendiff.format.json import format_json


FORMAT_FUNCTIONS = {'stylish': make_stylish,
                    'plain': make_plain,
                    'json': format_json,
                    }
DEFAULT_FORMAT_FUNCTIONS = 'stylish'

def generate_diff(path_file1: str,
                  path_file2: str,
                  format=DEFAULT_FORMAT_FUNCTIONS
                  ) -> str:

    old_data = get_value(path_file1)
    new_data = get_value(path_file2)

    if old_data == new_data:
        return ''

    values = get_diff(old_data, new_data)

    res = FORMAT_FUNCTIONS[format](values)

    return res
