    long long sum=0,min_sum=0;
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


