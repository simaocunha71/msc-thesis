    long long min_sum = numeric_limits<long long>::max();
    long long current_sum = 0;
    for (long long num : nums) {
        current_sum += num;
        min_sum = min(min_sum, current_sum);
        if (current_sum < 0) {
            current_sum = 0;
        }
    }
    return min_sum;
}