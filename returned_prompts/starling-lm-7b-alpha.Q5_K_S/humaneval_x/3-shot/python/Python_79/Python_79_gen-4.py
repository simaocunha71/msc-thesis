    def to_binary(decimal: int) -> str:
        result = ""
        while decimal:
            result += str(decimal % 2)
            decimal //= 2
        return result

    result = "db" + to_binary(decimal) + "db"
    return result


