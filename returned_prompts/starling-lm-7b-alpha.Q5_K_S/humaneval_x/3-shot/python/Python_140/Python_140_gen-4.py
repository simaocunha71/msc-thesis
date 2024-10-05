    result = []
    curr_space = False
    for c in text:
        if c == " ":
            if curr_space:
                result.append('-')
            else:
                curr_space = True
                result.append('_')
        else:
            curr_space = False
            result.append(c)
    return "".join(result)


