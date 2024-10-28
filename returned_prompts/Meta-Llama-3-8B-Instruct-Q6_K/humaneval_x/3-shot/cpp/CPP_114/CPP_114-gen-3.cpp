    long long min_sum=INT_MAX;
    long long sum=0;
    for (int i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        min_sum=min(min_sum,sum);
    }
    return min_sum;
} // This function does not work correctly, because it only considers subarrays that start at the first element. It should consider all subarrays, not just those that start at the first element.

