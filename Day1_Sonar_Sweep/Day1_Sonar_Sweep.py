def main():
    counter = 0
    with open("Day1_Sonar_Sweep/Day1_Sonar_Sweep.txt") as f:
        curr_list = []
        prev_list = []
        for line in f:
            if len(curr_list) == 3:
                prev_list = curr_list.copy()
                curr_list.pop(0)
            curr_list.append(int(line))
            if sum(curr_list) > sum(prev_list) and len(prev_list) == 3:
                counter += 1
            #     print(curr_list, prev_list, sum(curr_list), sum(prev_list), "Increased", counter)
            # elif sum(curr_list) < sum(prev_list):
            #     print(curr_list, prev_list, sum(curr_list), sum(prev_list), "Decreased")
            # else:
            #     print(curr_list, prev_list, sum(curr_list), sum(prev_list), "No change")
    print(counter)


if __name__ == "__main__":
    main()