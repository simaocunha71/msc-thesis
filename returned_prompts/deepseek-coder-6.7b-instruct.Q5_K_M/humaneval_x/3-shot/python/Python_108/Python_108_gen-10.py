    def sum_of_digits(n):
        total = 0
        while n:
            total, n = total + n % 10, n // 10
        return total

    return sum(sum_of_digits(num) > 0 for num in arr)


