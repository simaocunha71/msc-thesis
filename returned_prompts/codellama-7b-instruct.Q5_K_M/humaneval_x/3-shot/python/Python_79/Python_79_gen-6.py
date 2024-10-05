    if decimal == 0:
        return "db0db"
    if decimal == 1:
        return "db1db"

    result = ""
    while decimal > 0:
        if decimal % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        decimal = decimal // 2

    return "db" + result + "db"


