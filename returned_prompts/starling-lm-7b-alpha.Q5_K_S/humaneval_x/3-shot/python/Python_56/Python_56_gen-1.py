    result = 0
    for c in brackets:
        if c == "<":
            result += 1
        elif c == ">":
            result -= 1
            if result < 0:
                return False
    return result == 0


