    long long min = 0;
    long long sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        if (sum < min) {
            min = sum;
        }
        if (sum > 0) {
            sum = 0;
        }
    }
    return min;

}
int main() {
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(4);
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(4);
    long long a = minSubArraySum(nums);
    printf("%lld\n", a);
    return 0;
}
