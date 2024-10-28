    vector<int> order;
    vector<int> num;
    int i;
    int sum;
    for (i=0;i<nums.size();i++)
    {
        num=nums[i];
        sum=0;
        while (num!=0)
        {
            sum+=num%10;
            num/=10;
        }
        order.push_back(sum);
    }
    sort(order.begin(),order.end());
    vector<int> result;
    for (i=0;i<nums.size();i++)
    result.push_back(nums[i]);

    return result;
}

