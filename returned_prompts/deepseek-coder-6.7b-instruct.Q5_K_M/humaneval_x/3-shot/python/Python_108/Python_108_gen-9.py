    def sum_digits(n):
        if n > 0:
            return sum(int(digit) for digit in str(n))
        else:
            return sum(int(digit) for digit in str(n)[1:])

    return sum(sum_digits(x) > 0 for x in arr)


