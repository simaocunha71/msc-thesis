    def sum_digits(n: int) -> int:
        """ Sum of all digits of a non-negative integer """
        result = 0
        while n > 0:
            result += n % 10
            n = n // 10
        return result

    def signed_digits(n: int) -> int:
        """ Sum of all digits of an integer, considering the sign of each digit """
        sign = 1 if n >= 0 else -1
        result = 0
        while n > 0:
            result += (n % 10) * sign
            sign = -sign
            n = n // 10
        return result

    result = 0
    for elem in arr:
        if signed_digits(elem) > 0:
            result += 1

    return result


