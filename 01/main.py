distance = 0

def read_input():
    with open('input.txt') as f:
        return f.read().splitlines()

def split_line(line: str, separator: str):
    return line.split(separator)

def build_lists():
    l, r = [], []
    for line in read_input():
        numbers = split_line(line, '   ')
        l.append(int(numbers[0]))
        r.append(int(numbers[1]))

    return sorted(l), sorted(r)

if __name__ == '__main__':
    left, right = build_lists()

    for i in range(len(left)):
        distance += abs(left[i] - right[i])

    print(distance)
