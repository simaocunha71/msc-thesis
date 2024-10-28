    bracket_map = {"[": "]", "{": "}", "(": ")","<": ">"}
    open_brackets = set(["[", "{", "(", "<"])
    stack = []
    for i in string:
        if i in open_brackets:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True


