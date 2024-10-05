    result = "db"
    while decimal > 0:
        result += str(decimal % 2)
        decimal = decimal // 2
    return result + "db"


