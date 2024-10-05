    def sum_digits(n):
        if n < 0:
            return sum_digits(-n)
        else:
            return sum(map(int, str(n)))

    return sum(sum_digits(num) > 0 for num in arr)


