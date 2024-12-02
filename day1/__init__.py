from parsers import read_file
from .day1 import day1_part1, day1_part2

inputs = read_file("day1/data.txt")


def preprocess_data(items):

    new_list = []
    for pair in items:
        pair = pair.split("  ")
        d = []
        for i in pair:
            d.append(int(i.strip()))
        new_list.append(d)

    return new_list


def run_day1():
    items = preprocess_data(inputs)

    result1 = day1_part1(items)
    print("day1_part1 >>>>>>>>>>>>>>>>>>>>", result1)

    result2 = day1_part2(items)
    print("day1_part2 >>>>>>>>>>>>>>>>>>>>", result2)
