    def sum_digits(n):
        if n < 0:
            return sum_digits(-n)
        if n < 10:
            return n
        return n % 10 + sum_digits(n // 10)

    return sum(sum_digits(num) > 0 for num in arr)


