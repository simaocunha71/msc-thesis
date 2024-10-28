    vector<int> points;
    for (int i=0;i<nums.size();i++)
    {
        int sum=0;
        int temp=nums[i];
        while (temp>0)
        {
            sum+=temp%10;
            temp/=10;
        }
        points.push_back(sum);
    }
    for (int i=0;i<points.size();i++)
    {
        for (int j=i+1;j<points.size();j++)
        if (points[i]==points[j])
        if (nums[i]>nums[j])
        {
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
        }
    }
    return nums;
}

