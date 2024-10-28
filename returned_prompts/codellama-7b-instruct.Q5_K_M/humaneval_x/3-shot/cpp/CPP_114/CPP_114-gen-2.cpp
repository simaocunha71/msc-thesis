    long long min_sum=1000000000000000;
    long long current_sum=0;
    int i,j;
    for (i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        if (current_sum<min_sum)
        min_sum=current_sum;
        else
        {
        for (j=i+1;j<nums.size();j++)
        {
            current_sum+=nums[j];
            if (current_sum<min_sum)
            min_sum=current_sum;
            current_sum-=nums[i];
        }
        }
    }
    return min_sum;
}


