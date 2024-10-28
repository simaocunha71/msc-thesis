    long long sum = 1000000000000000000;
    long long curSum = 0;
    int i,j;
    for (i=0;i<nums.size();i++)
    {
        for (j=i;j<nums.size();j++)
        {
            curSum+=nums[j];
            if (curSum<sum) sum = curSum;
            if (curSum<0) curSum=0;
        }
        curSum=0;
    }
    return sum;
}


