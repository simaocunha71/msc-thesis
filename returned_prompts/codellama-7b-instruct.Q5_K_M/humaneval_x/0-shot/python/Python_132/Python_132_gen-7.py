
def is_nested(string):
    open_brackets = 0
    for char in string:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return False
    return open_brackets == 0