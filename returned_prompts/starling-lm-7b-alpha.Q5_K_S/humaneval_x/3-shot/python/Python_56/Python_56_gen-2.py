    opening_brackets = "([{"
    closing_brackets = ")]}"
    brackets_count = [0, 0, 0]
    for bracket in brackets:
        if bracket in opening_brackets:
            brackets_count[opening_brackets.index(bracket)] += 1
        elif bracket in closing_brackets:
            bracket_index = closing_brackets.index(bracket)
            if brackets_count[bracket_index] == 0:
                return False
            brackets_count[bracket_index] -= 1

    return True


