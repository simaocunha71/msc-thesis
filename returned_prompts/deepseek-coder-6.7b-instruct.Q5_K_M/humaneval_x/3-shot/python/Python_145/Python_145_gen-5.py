    def sum_digits(n):
        sum = 0
        n = abs(n)
        while n:
            sum += n % 10
            n //= 10
        return sum

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


