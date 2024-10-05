    vector<pair<int, int>> pairs;
    int i;
    for (i=0;i<nums.size();i++)
    {
        int sum_of_digits=0;
        int num=nums[i];
        while(num>0)
        {
            sum_of_digits+=num%10;
            num=num/10;
        }
        pairs.push_back({sum_of_digits, i});
    }
    sort(pairs.begin(), pairs.end());
    vector<int> result;
    for (i=0;i<pairs.size();i++)
    {
        result.push_back(nums[pairs[i].second]);
    }
    return result;
}