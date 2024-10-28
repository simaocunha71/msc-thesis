    long long i,j,min_sum=INT_MAX;
    for (i=0;i<nums.size();i++)
    {
        long long curr_sum=0;
        for (j=i;j<nums.size();j++)
        {
            curr_sum+=nums[j];
            if (curr_sum<min_sum)
            {
                min_sum=curr_sum;
            }
        }
    }
    return min_sum;
}


