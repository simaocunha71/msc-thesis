    long long min_sum=numeric_limits<long long>::max();
    long long current_sum=0;
    for (int i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        min_sum=min(min_sum,current_sum);
        if (current_sum<0)
            current_sum=0;
    }
    return min_sum;
}