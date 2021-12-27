class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ADJACENT = {
    "up": [-1, 0],
    "up_right": [-1, 1],
    "right": [0, 1],
    "down_right": [1, 1],
    "down": [1, 0],
    "down_left": [1, -1],
    "left": [0, -1],
    "up_left": [-1, -1]
}


def is_on_field(puzzle, point, changes):
    if (0 <= point.y + changes[0] < len(puzzle)
        and 0 <= point.x + changes[1] < len(puzzle[point.y + changes[0]])):
        return True
    return False


def do_flash(puzzle, point):
    for key in ADJACENT:
        if is_on_field(puzzle, point, ADJACENT[key]):
            new_point = Point(point.x + ADJACENT[key][1], point.y + ADJACENT[key][0])
            puzzle[new_point.y][new_point.x] += 1
    puzzle[point.y][point.x] = 0


def define_flash(puzzle):
    to_flash = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] >= 9:
                to_flash.append(Point(x, y))
    return to_flash


def make_step(puzzle):
    to_flash = define_flash(puzzle)
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] < 9:
                puzzle[y][x] += 1
    while to_flash:
        for point in to_flash:
            do_flash(puzzle, point)
        to_flash = define_flash(puzzle)


def main():
    puzzle = []
    steps = 100
    with open("Day11_Dumbo_Octopus/Day11_Dumbo_Octopus2.txt") as f:
        for line in f:
            puzzle.append(list(map(int, list(line.replace('\n', '')))))
    for step in range(steps):
        make_step(puzzle)
    print(puzzle)

if __name__ == "__main__":
    main()