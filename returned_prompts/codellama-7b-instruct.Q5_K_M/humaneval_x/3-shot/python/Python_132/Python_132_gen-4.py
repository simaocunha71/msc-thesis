    open_brackets = []
    for char in string:
        if char == '[':
            open_brackets.append(char)
        elif char == ']':
            if open_brackets:
                open_brackets.pop()
            else:
                return False
    return True if open_brackets else False


