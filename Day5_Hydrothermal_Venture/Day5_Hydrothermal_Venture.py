def get_range(p1, p2):
    if p1 > p2:
        step = -1
        p2 -= 1
    else:
        step = 1
        p2 += 1
    return p1, p2, step


def write_dots(diagram={}, dot=''):
    if diagram.get(dot):
        diagram[dot] += 1
    else:
        diagram[dot] = 1


def write_line(diagram={}, dot1='', dot2=''):
    x1, y1 = map(int, dot1.split(','))
    x2, y2 = map(int, dot2.split(','))
    if x1 == x2 and y1 == y2:
        # just dot
        write_dots(diagram, dot1)
    elif x1 == x2:
        # horizontal lines
        p1, p2, step = get_range(y1, y2)
        for y in range(p1, p2, step):
            write_dots(diagram, f'{x1},{y}')
    elif y1 == y2:
        # vertical lines
        p1, p2, step = get_range(x1, x2)
        for x in range(p1, p2, step):
            write_dots(diagram, f'{x},{y1}')
    elif abs(x1 - x2) == abs(y1 - y2):
        # diagonal lines
        px1, px2, step_x = get_range(x1, x2)
        _, _, step_y = get_range(y1, y2)
        for _ in range(px1, px2, step_x):
            write_dots(diagram, f'{x1},{y1}')
            x1 += step_x
            y1 += step_y
    else:
        # another type of lines
        pass


def main():
    diagram = {}
    with open("Day5_Hydrothermal_Venture/Day5_Hydrothermal_Venture.txt") as f:
        for line in f:
            dot1, dot2 = line.replace('\n', '').split(' -> ')
            write_line(diagram, dot1, dot2)
        values = list(diagram.values())
        dangerous = len(values) - values.count(1)
        print(dangerous)


if __name__ == "__main__":
    main()