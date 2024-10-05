
// minSubArraySum([1,2,3,4,5])
// minSubArraySum([1,2,3,4,5,6,7,8,9])
// minSubArraySum([1,2,3,4,5,6,7,8,9,10])

    long long min = nums[0];
    long long sum = 0;
    int i = 0;
    int j = 0;
    int count = nums.size();
    if (count == 0) return -1;
    while (i < count) {
        sum += nums[i];
        if (sum < min) min = sum;
        if (sum > min) {
            j = i;
            while (sum > min) {
                sum -= nums[j];
                j++;
            }
        }
        i++;
    }

    return min;
}
