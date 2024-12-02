from typing import Any


def day1_part1(data: list[Any]):
    left = []
    right = []
    for pair in data:
        left.append(pair[0])
        right.append(pair[1])

    left = sorted(left)
    right = sorted(right)

    somme = 0

    for i, _ in enumerate(left):
        somme += abs(left[i] - right[i])

    return somme


def day1_part2(data: list[Any]):
    left = []
    right = []
    for pair in data:
        left.append(pair[0])
        right.append(pair[1])

    similarity = 0
    for num in left:
        similarity += num * right.count(num)

    return similarity
