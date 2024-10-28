    long long min_sum=LLONG_MAX;
    long long sum=0;
    int i,j;
    for (i=0;i<nums.size();i++)
    for (j=i;j<nums.size();j++)
    {
        sum=0;
        for (int k=i;k<=j;k++)
        sum+=nums[k];
        if (sum<min_sum)
        min_sum=sum;
    }
    return min_sum;
}

