    vector<int> ordered_nums;
    for (int i=0;i<nums.size();i++)
    {
        int curr_num=nums[i];
        int sum=0;
        while (curr_num!=0)
        {
            sum+=curr_num%10;
            curr_num/=10;
        }
        int curr_sum=sum;
        for (int j=0;j<ordered_nums.size();j++)
        {
            if (curr_sum>sum)
                continue;
            else if (curr_sum<sum)
            {
                ordered_nums.insert(ordered_nums.begin()+j,curr_num);
                break;
            }
            else
                ordered_nums.insert(ordered_nums.begin()+j+1,curr_num);
        }
        if (ordered_nums.size()==i)
            ordered_nums.push_back(curr_num);
    }
    return ordered_nums;
}


