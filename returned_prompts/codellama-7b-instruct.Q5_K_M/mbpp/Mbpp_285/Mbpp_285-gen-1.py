
def text_match_two_three(my_string):
    if my_string.count("a") == 0:
        return False
    for i, c in enumerate(my_string):
        if c == "a":
            if i == len(my_string) - 1:
                return False
            if my_string[i + 1] == "b":
                if i == len(my_string) - 2:
                    return True
                if my_string[i + 2] == "b":
                    return True
            else:
                return False
    return False


