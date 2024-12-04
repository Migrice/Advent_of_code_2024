from parsers import read_file
from .day3 import day3_part1, day3_part2

inputs = read_file("day3/data.txt")


def run_day3():

    result1 = day3_part1(inputs)
    print("day3_part1 >>>>>>>>>>>>>>>>>>>>", result1)

    result2 = day3_part2(inputs)
    print("day3_part2 >>>>>>>>>>>>>>>>>>>>", result2)
