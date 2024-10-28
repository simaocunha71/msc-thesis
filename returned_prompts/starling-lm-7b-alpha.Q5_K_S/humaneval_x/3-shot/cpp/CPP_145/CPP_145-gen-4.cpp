    vector<int> all_nums;
    vector<int> result;
    int i;
    for (i=0;i<nums.size();i++)
    {
        int sum=0;
        string str=to_string(nums[i]);
        for (char chr:str)
        {
        sum+=int(chr)-48;
        }
        all_nums.push_back(sum);
        result.push_back(sum);
        result.push_back(nums[i]);
    }
    sort(all_nums.begin(),all_nums.end());
    sort(result.begin(),result.end());
    vector<int> final_result;
    for (i=0;i<all_nums.size();i++)
    {
        if (result[i]==all_nums[i])
        final_result.push_back(nums[i]);
    }
    return final_result;
}


