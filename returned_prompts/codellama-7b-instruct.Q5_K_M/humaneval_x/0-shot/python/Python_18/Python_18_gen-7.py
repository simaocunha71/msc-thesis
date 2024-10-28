
    count = 0
    while substring in string:
        count += 1
        string = string[string.index(substring) + 1:]
    return count



