    def sum_digits(n):
        n = abs(n)
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum

    return sorted(range(len(nums)), key=lambda i: (sum_digits(nums[i]), i))


