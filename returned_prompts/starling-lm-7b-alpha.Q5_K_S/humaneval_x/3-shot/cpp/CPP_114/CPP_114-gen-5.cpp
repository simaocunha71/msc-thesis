    long long i,sum,minsum=LLONG_MAX;
    for (i=0;i<nums.size();i++)
    {
        sum=0;
        for (int j=i;j<nums.size();j++)
        {
            sum+=nums[j];
            if (sum<minsum)
            minsum=sum;
        }
    }
    return minsum;
}



