import re

# data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def day3_part1(input: list[str]) -> int:
    data = "".join(input)

    p = re.compile("mul\(\d{1,3}\,\d{1,3}\)")
    word = re.compile("\d{1,3}")
    patterns = p.findall(data)
    somme = 0
    for pat in patterns:
        numbers = word.findall(pat)
        numbers = [int(n) for n in numbers]
        somme += numbers[0] * numbers[1]

    return somme


data = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()_don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(2,5)"
]

dat = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


def day3_part2(input):
    chaine = "".join(input)
    pat = re.compile(r"don't\(\).*?do\(\)")
    iterator = pat.finditer(chaine)

    indices = []
    for match in iterator:
        indices.append(match.span())

    result = []
    last_index = 0

    for start, end in indices:
        result.append(chaine[last_index:start])
        last_index = end

    result.append(chaine[last_index:])
    r = "".join(result)

    value = day3_part1([r])

    return value


print(day3_part2(data))
