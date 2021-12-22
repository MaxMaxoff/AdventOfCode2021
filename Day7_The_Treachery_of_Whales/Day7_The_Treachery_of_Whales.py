def get_arithmetic_sum(steps):
    return int((((2) + (steps - 1)) / 2) * steps)


def get_lowest(initial_list):
    min_sum_part_one = max(initial_list)**2
    min_sum_part_two = max(initial_list)**3
    for idx in range(min(initial_list), max(initial_list) + 1):
        current_sum_part_one = 0
        current_sum_part_two = 0
        for item in initial_list:
            current_sum_part_one += abs(item - idx)
            current_sum_part_two += get_arithmetic_sum(abs(item - idx))
        if current_sum_part_one < min_sum_part_one:
            min_sum_part_one = current_sum_part_one
        if current_sum_part_two < min_sum_part_two:
            min_sum_part_two = current_sum_part_two
    return min_sum_part_one, min_sum_part_two


def main():
    with open("Day7_The_Treachery_of_Whales/Day7_The_Treachery_of_Whales.txt"
              ) as f:
        initial_list = list(map(int, f.readline().split(',')))
    print(get_lowest(initial_list))


if __name__ == "__main__":
    main()