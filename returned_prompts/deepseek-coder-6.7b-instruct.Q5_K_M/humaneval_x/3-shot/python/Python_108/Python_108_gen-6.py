    def sum_of_digits(n):
        digits = list(map(int, str(n)))
        return sum(digits)

    return sum(sum_of_digits(n) > 0 for n in arr)


