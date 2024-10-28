    def is_odd(x):
        return x % 2 == 1

    def is_positive_integer(x):
        return x >= 0 and x.is_integer()

    result = 0
    for num in lst:
        if is_odd(num) and is_positive_integer(num):
            result += num ** 2

    return result

