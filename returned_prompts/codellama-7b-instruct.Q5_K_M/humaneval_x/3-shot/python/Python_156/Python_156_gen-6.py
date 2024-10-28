    mapping = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    result = ""
    for i in range(1, 1000, 100):
        if number >= i:
            result += mapping[i]
            number -= i

    for i in range(1, 50, 10):
        if number >= i:
            result += mapping[i]
            number -= i

    for i in range(1, 5, 1):
        if number >= i:
            result += mapping[i]
            number -= i

    return result


