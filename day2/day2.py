# data = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]


def is_sorted(list_data: list[int]) -> bool:
    return bool(
        all(list_data[i] <= list_data[i + 1] for i in range(len(list_data) - 1))
        or all(list_data[i] >= list_data[i + 1] for i in range(len(list_data) - 1))
    )


def is_less_than_3_and_greater_than_1(list_data: list[int]):
    distances = []
    for i in range(len(list_data) - 1):
        distances.append(abs(list_data[i] - list_data[i + 1]))

    return bool(
        all(distances[i] >= 1 and distances[i] <= 3 for i in range(len(distances)))
    )


def day2_part1(rule: list[int]) -> int:
    return 1 if is_sorted(rule) and is_less_than_3_and_greater_than_1(rule) else 0