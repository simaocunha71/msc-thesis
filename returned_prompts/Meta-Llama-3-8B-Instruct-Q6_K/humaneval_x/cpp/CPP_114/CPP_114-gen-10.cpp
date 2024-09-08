    long long res = 1e18;
    long long curr_sum = 0;
    for(long long i = 0; i < nums.size(); i++){
        curr_sum += nums[i];
        res = min(res, curr_sum);
        if(curr_sum < 0) curr_sum = 0;
    }
    return res;
}

int main()
{
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    long long res = minSubArraySum(nums);
    printf("Minimum sub-array sum: %lld\n", res);
    return 0;
}
