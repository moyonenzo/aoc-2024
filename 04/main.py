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
        if word == 'XMAS':
            return True
        return False
    except IndexError:
        return False

def valid_from_count(array: list[list[str]], x: int, y: int):
    right = [(x, y), (x+1, y), (x+2, y), (x+3, y)]
    left = [(x, y), (x-1, y), (x-2, y), (x-3, y)]
    top = [(x, y), (x, y-1), (x, y-2), (x, y-3)]
    bottom = [(x, y), (x, y+1), (x, y+2), (x, y+3)]
    br = [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]
    bl = [(x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3)]
    tr = [(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)]
    tl = [(x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)]

    return (
        list(
            map(lambda k: is_valid(array, k), [right, left, top, bottom, br, bl, tr, tl])
        ).count(True)
    )


if __name__ == '__main__':
    count = 0
    array = arrayse(read_input())

    for y in range(len(array)):
        for x in range(len(array[y])):
            count += valid_from_count(array, x, y)

    print(count)