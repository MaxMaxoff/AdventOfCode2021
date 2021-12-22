def get_gamma_epsilon(diagnostic_list=[]):
    common_list = []
    for line in diagnostic_list:
        if not len(common_list):
            common_list = [0 for i in range(len(line))]
        for idx in range(len(common_list)):
            if line[idx] == '1':
                common_list[idx] += 1
            elif line[idx] == '0':
                common_list[idx] -= 1
    gamma_list = []
    epsilon_list = []
    for item in common_list:
        if item > 0:
            gamma_list.append('1')
            epsilon_list.append('0')
        elif item < 0:
            gamma_list.append('0')
            epsilon_list.append('1')
    gamma = ''.join(gamma_list)
    epsilon = ''.join(epsilon_list)
    return gamma, epsilon


def get_rating(diagnostic_list=[], oxygen=True, idx=0):
    one_list = []
    zero_list = []
    for line in diagnostic_list:
        if line[idx] == '1':
            one_list.append(line)
        else:
            zero_list.append(line)
    if oxygen:
        if len(one_list) == len(zero_list) == 1:
            return ''.join(one_list if one_list[0][idx] == '1' else zero_list)
        else:
            return get_rating(one_list if len(one_list) >= len(zero_list) else zero_list, oxygen, idx + 1)
    else:
        if len(one_list) == len(zero_list) == 1:
            return ''.join(one_list if one_list[0][idx] == '0' else zero_list)
        else:
            return get_rating(one_list if len(one_list) <= len(zero_list) else zero_list, oxygen, idx + 1)


def main():
    with open("Day3_Binary_Diagnostic/Day3_Binary_Diagnostic.txt") as f:
        diagnostic_list = []
        for line in f:
            diagnostic_list.append(line.replace('\n', ''))
        gamma, epsilon = get_gamma_epsilon(diagnostic_list)
        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        print(gamma * epsilon)

        oxygen = get_rating(diagnostic_list, True)
        CO2 = get_rating(diagnostic_list, False)
        print(int(oxygen, 2) * int(CO2, 2))


if __name__ == "__main__":
    main()