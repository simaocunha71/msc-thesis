    long long min_sum=1000000000000000;
    long long curr_sum=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        curr_sum+=nums[i];
        if (curr_sum<min_sum)
        min_sum=curr_sum;
        if (curr_sum<0)
        curr_sum=0;
    }
    return min_sum;
}



