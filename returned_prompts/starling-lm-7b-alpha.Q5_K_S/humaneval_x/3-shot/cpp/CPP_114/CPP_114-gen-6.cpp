    long long curr_sum = nums[0];
    long long min_sum = nums[0];
    int i;
    for (i=1;i<nums.size();i++)
    {
        curr_sum = min(nums[i], curr_sum+nums[i]);
        min_sum = min(min_sum, curr_sum);
    }
    return min_sum;
}



