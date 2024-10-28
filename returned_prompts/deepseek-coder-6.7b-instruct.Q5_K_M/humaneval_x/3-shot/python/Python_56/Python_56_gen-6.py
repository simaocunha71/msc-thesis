    counter = 0
    for bracket in brackets:
        if bracket == '<':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


