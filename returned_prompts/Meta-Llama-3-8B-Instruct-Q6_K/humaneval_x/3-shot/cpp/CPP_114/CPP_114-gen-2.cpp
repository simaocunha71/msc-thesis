    long long min_sum=LONG_LONG_MAX;
    long long current_sum=0;
    for (long long i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        min_sum=min(min_sum,current_sum);
        if (current_sum<0)
            current_sum=0;
    }
    return min_sum;
}