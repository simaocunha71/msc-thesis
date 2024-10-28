    long long result=1000000000000000000;
    long long sum=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        if (sum<result)
        result=sum;
        if (sum<0)
        sum=0;
    }
    return result;
}



