    result = ""

    for idx1, idx2 in zip(a, b):
        if idx1 == idx2:
            result += "0"
        else:
            result += "1"

    return result


