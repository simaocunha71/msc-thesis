    def sum_digits(n):
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res

    result = 0
    for elem in arr:
        if sum_digits(elem) > 0:
            result += 1
    return result


