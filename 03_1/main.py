import re

def read_input() -> str:
    with open('input.txt') as f:
        return f.read()

def matches(s: str) -> list[str]:
    return re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", s)

def split_match(s: str) -> tuple[int, int]:
    splitted = s.split(",")
    return int(splitted[0][4::]), int(splitted[1][:-1])

def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    matches = matches(read_input())
    total = 0

    last_instruction = "do()"
    for match in matches:
        if "mul" in match and last_instruction == "do()":
            total += multiply(*split_match(match))
        elif match in ["do()", "don't()"]:
            last_instruction = match

    print(total)