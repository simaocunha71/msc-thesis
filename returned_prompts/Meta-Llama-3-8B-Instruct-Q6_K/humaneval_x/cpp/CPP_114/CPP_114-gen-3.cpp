    long long sum = 0;
    long long min_sum = LONG_LONG_MAX;
    for(long long i = 0; i < nums.size(); i++){
        sum = 0;
        for(long long j = i; j < nums.size(); j++){
            sum += nums[j];
            min_sum = min(min_sum, sum);
        }
    }
    return min_sum;
}

int main()
{
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums)); // Output: 1
    return 0;
}

B:
    long long minSubArraySum(vector<long long> nums){
        long long min_sum = LONG_LONG_MAX;
        long long curr_sum = 0;
        for(long long i = 0; i < nums.size(); i++){
            curr_sum += nums[i];
            min_sum = min(min_sum, curr_sum);
            if(curr_sum > 0){
                curr_sum = 0;
            }
        }
        return min_sum;
    }
    
    int main()
    {
        vector<long long> nums = {2, 3, 4, 1, 2, 4};
        printf("%lld\n", minSubArraySum(nums)); // Output: 1
        return 0;
    }
C:
    long long minSubArraySum(vector<long long> nums){
        long long min_sum = LONG_LONG_MAX;
        long long curr_sum = 0;
        for(long long i = 0; i < nums.size(); i++){
            curr_sum += nums[i];
            min_sum = min(min_sum, curr_sum);
            if(curr_sum < 0){
                curr_sum = 0;
            }
        }
        return min_sum;
    }
    
    int main()
    {
        vector<long long> nums = {2, 3, 4, 1, 2, 4};
        printf("%lld\n", minSubArraySum(nums)); // Output: 1
        return 0;
    }
D:
    long long minSubArraySum(vector<long long> nums){
        long long min_sum = LONG_LONG_MAX;
        long long curr_sum = 0;
        for(long long i = 0; i < nums.size(); i++){
            curr_sum += nums[i];
            min_sum = min(min_sum, curr_sum);
        }
        return min_sum;
   