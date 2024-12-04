def read_input() -> str:
    with open('input.txt') as f:
        return f.read()

def arrayse(input: str) -> list[list[str]]:
    array = []
    for line in input.splitlines():
        array.append([ *line ])

    return array

def is_valid(array: list[list[str]], sequence: list[tuple[int, int]]) -> bool:
    try:
        if any(c[0] < 0 or c[1] < 0 for c in sequence):
            raise IndexError

        word = ''
        for coordinates in sequence:
            word += array[coordinates[1]][coordinates[0]]

        if word == 'MAS':
            return True
        return False
    except IndexError:
        return False

def valid_from(array: list[list[str]], x: int, y: int):
    if array[y][x] != 'A':
        return False

    sequences = [
        [(x - 1, y - 1), (x, y), (x + 1, y + 1)],
        [(x + 1, y + 1), (x, y), (x - 1, y - 1)],
        [(x - 1, y + 1), (x, y), (x + 1, y - 1)],
        [(x + 1, y - 1), (x, y), (x - 1, y + 1)],
    ]

    valids = list(map(lambda k: is_valid(array, k), sequences)).count(True)
    if valids < 2:
        return False
    return True


if __name__ == '__main__':
    count = 0
    array = arrayse(read_input())

    for y in range(len(array)):
        for x in range(len(array[y])):
            if valid_from(array, x, y): count += 1

    print(count)
