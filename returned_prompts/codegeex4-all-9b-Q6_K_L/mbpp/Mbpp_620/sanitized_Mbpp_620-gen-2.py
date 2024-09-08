def largest_subset(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    if not numbers:
        return 0

    numbers.sort()
    dp = [1] * len(numbers)
    max_size = 1

    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] % numbers[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_size = max(max_size, dp[i])

    return max_size