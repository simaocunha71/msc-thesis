    vector<int> sorted_nums;
    vector<pair<int,int>> num_and_idx;
    for (int i=0;i<nums.size();i++)
    {
        int sum=0;
        int num=nums[i];
        while (num!=0)
        {
            sum+=num%10;
            num/=10;
        }
        num_and_idx.push_back(make_pair(sum, i));
    }
    sort(num_and_idx.begin(), num_and_idx.end());
    for (int i=0;i<num_and_idx.size();i++)
    sorted_nums.push_back(nums[num_and_idx[i].second]);
    return sorted_nums;
}



