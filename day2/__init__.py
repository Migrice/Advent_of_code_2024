from parsers import read_file
from .day2 import day2_part1

inputs = read_file("day2/data.txt")


def preprocess_data(items):
    data = []
    items_in_list = [item.split(" ") for item in items]
    for item in items_in_list:
        data.append(list(map(int, item)))

    return data


def run_day2():
    input_data = preprocess_data(inputs)
    result1 = sum([day2_part1(rule) for rule in input_data])

    print("day2_part1 >>>>>>>>>>>>>>>>>>>>", result1)
