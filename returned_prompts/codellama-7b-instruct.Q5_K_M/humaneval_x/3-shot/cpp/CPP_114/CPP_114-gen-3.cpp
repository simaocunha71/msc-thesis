    long long min_sum=0;
    long long sum=0;
    long long i=0;
    long long j=0;
    long long current_sum=0;
    for (i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        current_sum=sum;
        for (j=i+1;j<nums.size();j++)
        {
            sum+=nums[j];
            if (sum<current_sum)
            {
                current_sum=sum;
            }
        }
        if (current_sum<min_sum || i==0)
        {
            min_sum=current_sum;
        }
        sum=0;
    }
    return min_sum;
}



