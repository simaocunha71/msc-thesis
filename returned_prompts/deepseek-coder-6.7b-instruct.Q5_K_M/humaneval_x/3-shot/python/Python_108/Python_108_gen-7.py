    def sum_digits(n):
        return sum(int(d) for d in str(n))

    return sum(sum_digits(n) > 0 for n in arr)


