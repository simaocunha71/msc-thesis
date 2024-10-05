    def get_digit_name(digit):
        return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][digit - 1]

    result = []
    for i in arr:
        if i > 0 and i < 10:
            result.append(get_digit_name(i))

    return result[::-1] if result else []