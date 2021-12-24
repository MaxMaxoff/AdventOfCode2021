from os import terminal_size


def check_brackets(string=''):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    complete_score_dict = {')': 1, ']': 2, '}': 3, '>': 4}

    score = 0
    complete_score = 0
    brackets_ok = True

    for symbol in string:
        if symbol in brackets.keys():
            stack.append(symbol)
        elif symbol in brackets.values():
            if stack:
                bracket = stack.pop()
                if brackets.get(bracket) != symbol:
                    print(
                        f' - {string} - Expected {brackets.get(bracket)}, but found {symbol} instead.'
                    )
                    score += score_dict[symbol]
                    brackets_ok = False
                    break
            # Stack is empty, but opened symbol found
            # else:
            #     break

    # Stack is not empty
    if stack and brackets_ok:
        complete_stack = []
        for item in stack[::-1]:
            complete_stack.append(brackets.get(item))
            complete_score = complete_score * 5 + complete_score_dict[
                brackets.get(item)]
        stack_string = ''.join(complete_stack)
        print(
            f' - {string} - Complete by adding {stack_string} - {complete_score} total points.'
        )

    return score, complete_score


def main():
    score = 0
    middle_score = []
    with open("Day10_Syntax_Scoring/Day10_Syntax_Scoring.txt") as f:
        for line in f:
            cur_score, cur_complete_score = check_brackets(
                line.replace('\n', ''))
            score += cur_score
            if cur_complete_score != 0:
                middle_score.append(cur_complete_score)

    print(score, sorted(middle_score)[len(middle_score) // 2])


if __name__ == "__main__":
    main()