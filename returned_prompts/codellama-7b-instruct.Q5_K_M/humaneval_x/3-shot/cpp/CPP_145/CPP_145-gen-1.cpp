    int i,j;
    vector<int> sorted_nums;
    vector<vector<int>> parts;
    vector<int> part;
    int max_sum=0;
    int current_sum=0;
    int temp;
    for (i=0;i<nums.size();i++)
    {
        current_sum=0;
        for (j=0;j<nums[i];j++)
        {
            current_sum+=nums[i];
        }
        if (current_sum>max_sum)
        {
            max_sum=current_sum;
        }
    }

    for (i=0;i<nums.size();i++)
    {
        current_sum=0;
        for (j=0;j<nums[i];j++)
        {
            current_sum+=nums[i];
        }
        if (current_sum==max_sum)
        {
            part.push_back(nums[i]);
        }
    }
    parts.push_back(part);
    temp=0;
    for (i=0;i<parts.size();i++)
    {
        for (j=0;j<parts[i].size();j++)
        {
            if (temp<parts[i][j])
            {
                temp=parts[i][j];
            }
        }
        sorted_nums.push_back(temp);
    }
    return sorted_nums;
}


