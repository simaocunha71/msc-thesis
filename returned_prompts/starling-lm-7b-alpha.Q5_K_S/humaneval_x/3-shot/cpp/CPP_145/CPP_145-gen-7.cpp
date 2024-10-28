    vector<int> ordered_nums;
    int i;
    for (i=0;i<nums.size();i++)
    ordered_nums.push_back(nums[i]);

    int j,k;
    int tmp;
    for (i=0;i<ordered_nums.size()-1;i++)
    for (j=i+1;j<ordered_nums.size();j++)
    {
        int sum1=0,sum2=0;
        int idx1=ordered_nums[i];
        int idx2=ordered_nums[j];

        while (idx1!=0)
        {
            sum1+=idx1%10;
            idx1/=10;
        }
        while (idx2!=0)
        {
            sum2+=idx2%10;
            idx2/=10;
        }
        if (sum1<sum2||(sum1==sum2&&i>j))
        {
            tmp=ordered_nums[i];
            ordered_nums[i]=ordered_nums[j];
            ordered_nums[j]=tmp;
        }
    }
    return ordered_nums;
}



