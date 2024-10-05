    count = 0
    for bracket in brackets:
        if bracket == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return count == 0


