    long long min_sum=INT_MAX,cur_sum=0;
    int i,j,k;
    for (i=0;i<nums.size();i++)
    {
        cur_sum=0;
        for (j=i;j<nums.size();j++)
        {
            cur_sum+=nums[j];
            if (cur_sum<min_sum)
                min_sum=cur_sum;
        }
    }
    return min_sum;
}


