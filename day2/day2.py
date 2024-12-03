import copy


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


def day2_part2(input: list[int]) -> int:
    rule = copy.deepcopy(input)
    result = 0

    if is_sorted(rule) and is_less_than_3_and_greater_than_1(rule):
        result = 1

    else:
        i = 0

        while i < (len(rule)):
            temporary_rule = rule[:i] + rule[i + 1 :]
            if is_sorted(temporary_rule) and is_less_than_3_and_greater_than_1(
                temporary_rule
            ):
                result = 1
                break
            i += 1

    return result
