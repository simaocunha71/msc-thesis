    long long min_sum=INT_MAX;
    long long sum=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        if (sum<min_sum)
        min_sum=sum;
        if (sum<0)
        sum=0;
    }
    return min_sum;
}


