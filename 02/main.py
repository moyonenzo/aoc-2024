def read_input() -> list[str]:
    with open('input.txt') as f:
        return f.read().splitlines()

def split_line(line: str, separator: str) -> list[int]:
    return list(map(lambda k: int(k), line.split(separator)))


def is_safe(levels: list[int]) -> bool:
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    for i in range(len(levels)):
        try:
            if abs(levels[i] - levels[i + 1]) not in [1, 2, 3]:
                return False
        except IndexError:
            pass

    return True

if __name__ == '__main__':
    safe_count = 0

    for line in read_input():
        if is_safe(split_line(line, ' ')):
            safe_count += 1

    print(safe_count)
