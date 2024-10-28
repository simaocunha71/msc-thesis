    long long min=0, sum=0;
    int i=0, j=0;
    while (j<nums.size())
    {
        sum+=nums[j];
        if (sum<min)
        min=sum;
        if (sum<0)
        sum=0;
        j+=1;
    }
    return min;
}



