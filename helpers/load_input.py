import os


def load_input(file_name: str) -> str:
    with open(
        os.path.join(os.path.dirname(__file__), "..", "inputs", file_name), "r"
    ) as file:
        data = [line.strip() for line in file.readlines()]
    return data
