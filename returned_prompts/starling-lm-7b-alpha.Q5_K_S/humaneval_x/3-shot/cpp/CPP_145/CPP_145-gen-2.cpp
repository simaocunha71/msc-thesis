    vector<int> all_nums;
    int i;
    for (i=0;i<nums.size();i++)
    {
        int current_num=nums[i];
        int sum=0;
        while (current_num>0)
        {
            sum+=current_num%10;
            current_num/=10;
        }
        all_nums.push_back(sum);
    }
    sort(all_nums.begin(),all_nums.end());
    vector<int> order;
    for (i=0;i<all_nums.size();i++)
    {
        int index=nums.size();
        for (int j=0;j<nums.size();j++)
        {
            if (all_nums[i]==nums[j])
            {
                index=j;
                break;
            }
        }
        order.push_back(index);
    }
    return order;
}


