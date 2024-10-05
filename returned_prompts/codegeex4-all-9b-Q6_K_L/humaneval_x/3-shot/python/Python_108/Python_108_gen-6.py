    def sum_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sum(1 for num in arr if sum_digits(num) > 0)

