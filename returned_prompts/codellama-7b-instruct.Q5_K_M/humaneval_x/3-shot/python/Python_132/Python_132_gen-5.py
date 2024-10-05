    open_brackets = 0
    for i in range(len(string)):
        if string[i] == '[':
            open_brackets += 1
        elif string[i] == ']':
            open_brackets -= 1
        if open_brackets < 0:
            return False
    if open_brackets != 0:
        return False
    else:
        return True


