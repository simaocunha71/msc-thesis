    def sum_digits(n):
        if n < 0:
            n = -n
        return sum(int(digit) for digit in str(n))

    return sum(1 for num in arr if sum_digits(num) > 0)  # Count numbers with sum of digits > 0


