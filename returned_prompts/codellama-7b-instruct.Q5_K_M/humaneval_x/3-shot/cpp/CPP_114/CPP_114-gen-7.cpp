    long long min_sum=nums[0];
    long long current_sum=nums[0];
    int i,j;
    for (i=1;i<nums.size();i++)
    {
        current_sum+=nums[i];
        if (current_sum<min_sum)
        min_sum=current_sum;
        else if (current_sum>min_sum)
        current_sum=0;
    }
    return min_sum;
}


