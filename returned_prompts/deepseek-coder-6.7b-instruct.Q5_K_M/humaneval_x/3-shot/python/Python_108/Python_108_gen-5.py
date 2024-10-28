    def sum_of_digits(n):
        """Return the sum of the digits of n."""
        s = 0
        while n:
            s, n = s + n % 10, n // 10
        return s

    return sum(sum_of_digits(x) > 0 for x in arr)


