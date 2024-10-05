    count = 0
    for bracket in brackets:
        if bracket == '<':
            count += 1
        elif bracket == '>':
            count -= 1
        if count < 0:  # if we encounter a closing bracket before an opening one
            return False
    return count == 0  # if there are unmatched opening brackets


