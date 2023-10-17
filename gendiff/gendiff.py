from gendiff.get_diff import *
from gendiff.parse_data import get_value
from gendiff.format.stylish import make_stylish
from gendiff.format.plain import make_plain
from gendiff.format.json import format_json


def generate_diff(path_file1: str,
                  path_file2: str,
                  format=make_stylish
                  ) -> str:

    old_data = get_value(path_file1)
    new_data = get_value(path_file2)

    if old_data == new_data:
        return ''

    values = get_diff(old_data, new_data)

    res = FORMAT_FUNCTIONS[format](values)

    return res
