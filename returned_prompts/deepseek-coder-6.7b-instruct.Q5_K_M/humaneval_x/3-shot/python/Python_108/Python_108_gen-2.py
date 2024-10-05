    def sum_digits(n):
        sum = 0
        while n:
            digit = n % 10
            sum += digit
            n //= 10
        return sum

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count


