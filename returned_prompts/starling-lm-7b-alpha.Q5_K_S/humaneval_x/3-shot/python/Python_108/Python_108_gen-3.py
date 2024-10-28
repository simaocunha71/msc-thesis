    def sum_digits(n):
        return sum(map(int, str(abs(n))))

    result = 0
    for elem in arr:
        if sum_digits(elem) > 0:
            result += 1
    return result


