    long long sum=0;
    long long min_sum=0;
    long long i=0;
    long long j=0;
    for (i=0;i<nums.size();i++)
    {
    sum+=nums[i];
    min_sum=min(sum,min_sum);
    while (sum>sum)
    {
    sum-=nums[j];
    j+=1;
    }
    }
    return min_sum;
}


