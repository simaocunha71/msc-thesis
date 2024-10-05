    long long min_sum=999999999999999999ll;
    long long current_sum=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        if (current_sum<min_sum)
        min_sum=current_sum;
        if (current_sum<0)
        current_sum=0;
    }
    return min_sum;
}



