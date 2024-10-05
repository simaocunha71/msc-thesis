    long long sum=0;
    for (int i=0;i<nums.size();i++)
    {
        sum+=nums[i];
        for (int j=i+1;j<nums.size();j++)
        {
            sum+=nums[j];
            if (sum<0)
            sum=0;
            else
            break;
        }
    }
    return sum;
}


