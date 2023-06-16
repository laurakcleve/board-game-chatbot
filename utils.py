from datetime import datetime
import json


def get_timestamp_str():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def log(data, output_dir, suffix):
    with open(f"{output_dir}/{get_timestamp_str()}_{suffix}.json", "w") as file:
        file.write(json.dumps(data))
