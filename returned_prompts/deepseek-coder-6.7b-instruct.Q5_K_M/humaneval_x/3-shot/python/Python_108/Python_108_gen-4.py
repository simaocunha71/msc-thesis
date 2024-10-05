    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    return sum(sum_digits(num) > 0 for num in arr)

