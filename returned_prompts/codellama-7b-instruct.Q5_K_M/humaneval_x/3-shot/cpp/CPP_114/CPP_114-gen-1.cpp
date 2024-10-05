    int i,j;
    long long min_sum=0;
    long long current_sum=0;
    long long current_min=0;
    for (i=0;i<nums.size();i++)
    {
    current_sum+=nums[i];
    current_min=min(current_sum,current_min);
    if (current_sum<0)
    current_sum=0;
    if (i==nums.size()-1)
    min_sum=min(min_sum,current_min);
    }
    return min_sum;
}



