    vector<pair<int, int>> pairs;
    for (int i=0; i<nums.size(); i++)
    {
        int sum = 0;
        int num = nums[i];
        while (num > 0)
        {
            sum += num % 10;
            num /= 10;
        }
        pairs.push_back(make_pair(sum, i));
    }
    sort(pairs.begin(), pairs.end());
    vector<int> result;
    for (int i=0; i<pairs.size(); i++)
    {
        result.push_back(nums[pairs[i].second]);
    }
    return result;
}*/



