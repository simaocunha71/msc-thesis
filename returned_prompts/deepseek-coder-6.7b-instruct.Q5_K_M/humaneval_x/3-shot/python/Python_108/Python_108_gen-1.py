    def sum_of_digits(n):
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum

    return sum(1 for num in arr if sum_of_digits(num) > 0)


