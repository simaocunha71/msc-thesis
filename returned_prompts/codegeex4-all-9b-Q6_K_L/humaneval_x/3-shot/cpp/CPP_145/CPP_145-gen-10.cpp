    int i,j;
    vector<int> temp=nums;
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    {
        int sum1=0,sum2=0;
        int temp1=temp[i],temp2=temp[j];
        while(temp1>0)
        {
            sum1+=temp1%10;
            temp1/=10;
        }
        while(temp2>0)
        {
            sum2+=temp2%10;
            temp2/=10;
        }
        if (sum1>sum2)
        {
            swap(temp[i],temp[j]);
        }
    }
    return temp;
}

