    long long sum = 0, minSum = LONG_LONG_MAX;
    for (long long num : nums) {
        sum += num;
        minSum = min(minSum, sum);
        if (sum < 0) sum = 0;
    }
    return minSum;
}