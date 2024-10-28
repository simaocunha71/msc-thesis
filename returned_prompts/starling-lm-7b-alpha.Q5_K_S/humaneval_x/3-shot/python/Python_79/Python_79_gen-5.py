    def to_binary(n, length):
        if n == 0:
            return "0" * length
        result = ""
        while n > 0:
            result += str(n % 2)
            n //= 2
        return result

    result = to_binary(decimal, 8 * len(str(decimal)) + 2)
    return "db" + result + "db"


