    count = 0
    for b in brackets:
        if b == '<':
            count += 1
        elif b == '>':
            if count == 0:
                return False
            count -= 1
    return count == 0


