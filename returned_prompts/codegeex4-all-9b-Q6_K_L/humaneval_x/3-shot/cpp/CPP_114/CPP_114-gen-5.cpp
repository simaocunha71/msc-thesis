    long long min=nums[0],sum=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        if (sum<min)
        min=sum;
        if (sum>0)
        sum=0;
    }
    return min;
}

