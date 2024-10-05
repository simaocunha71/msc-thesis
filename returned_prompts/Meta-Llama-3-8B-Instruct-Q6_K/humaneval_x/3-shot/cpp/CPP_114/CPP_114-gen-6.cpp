    long long sum = 0, minSum = numeric_limits<long long>::max();
    for (long long num : nums) {
        sum += num;
        minSum = min(minSum, sum);
        if (sum < 0) sum = 0;
    }
    return minSum;
}
// OR
#include <algorithm>
long long minSubArraySum(vector<long long> nums) {
    long long minSum = numeric_limits<long long>::max();
    for (long long num : nums) {
        minSum = min(minSum, accumulate(nums.begin(), nums.end(), 0LL));
        nums[nums.begin() + accumulate(nums.begin(), nums.end(), 0LL) - num]++;
    }
    return minSum;
}
// OR
long long minSubArraySum(vector<long long> nums) {
    long long res = 0, temp = 0;
    for (long long num : nums) {
        temp += num;
        res = min(res, temp);
        if (temp < 0) temp = 0;
    }
    return res;
}
// OR
long long minSubArraySum(vector<long long> nums) {
    long long res = 0, sum = 0;
    for (long long num : nums) {
        sum += num;
        res = min(res, sum);
        if (sum > 0) sum = 0;
    }
    return res;
} 
// OR
long long minSubArraySum(vector<long long> nums) {
    long long res = LONG_LONG_MAX, sum = 0;
    for (long long num : nums) {
        sum += num;
        res = min(res, sum);
        if (sum > 0) sum = 0;
    }
    return res;
} 
// OR
long long minSubArraySum(vector<long long> nums) {
    long long res = numeric_limits<long long>::max(), sum = 0;
    for (long long num : nums) {
        sum += num;
        res = min(res, sum);
    }
    return res;
} 
// OR
long long minSubArraySum(vector<long long> nums) {
    long long res = 0, sum = 0;
    for (long long num : nums) {
        sum += num;
        res = min(res, sum);
    }
    return res;
} 
// OR
long long minSubArraySum(vector<long long> nums