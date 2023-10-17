import json


def format_json(data: dict) -> str:

    return json.dumps(data, sort_keys=True, indent=4)
