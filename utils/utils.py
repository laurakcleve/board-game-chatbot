from datetime import datetime
import json
from fuzzywuzzy import fuzz


def get_timestamp_str():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def log(data, output_dir, suffix):
    with open(f"{output_dir}/{get_timestamp_str()}_{suffix}.json", "w") as file:
        file.write(json.dumps(data))


def print_ratios(text1, text2):
    print(f"ratio: {fuzz.ratio(text1, text2)}")
    print(f"partial_ratio: {fuzz.partial_ratio(text1, text2)}")
    print(f"token_sort_ratio: {fuzz.token_sort_ratio(text1, text2)}")
    print(f"token_set_ratio: {fuzz.token_set_ratio(text1, text2)}")
    print(f"partial_token_sort_ratio: {fuzz.partial_token_sort_ratio(text1, text2)}")
    print(f"partial_token_set_ratio: {fuzz.partial_token_set_ratio(text1, text2)}")
