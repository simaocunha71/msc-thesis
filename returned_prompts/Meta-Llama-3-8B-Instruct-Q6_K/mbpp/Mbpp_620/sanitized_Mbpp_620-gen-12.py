def largest_subset(numbers):
    numbers.sort()
    dp = [1] * len(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] % numbers[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)