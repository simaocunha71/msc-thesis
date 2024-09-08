    long long min_sum = nums[0];
    long long current_sum = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        current_sum += nums[i];
        min_sum = min(min_sum, current_sum);
        if (current_sum < 0) {
            current_sum = 0;
        }
    }
    return min_sum;
}

int main() {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    long long result = minSubArraySum(nums);
    printf("Minimum sum of any non-empty sub-vector: %lld\n", result);
    return 0;
}
