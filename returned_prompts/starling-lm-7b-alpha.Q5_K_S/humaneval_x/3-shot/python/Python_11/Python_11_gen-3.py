    result = ""
    for a_char, b_char in zip(a, b):
        if a_char == "0" and b_char == "0":
            result += "0"
        elif a_char == "0" and b_char == "1":
            result += "1"
        elif a_char == "1" and b_char == "0":
            result += "1"
        elif a_char == "1" and b_char == "1":
            result += "0"

    return result


