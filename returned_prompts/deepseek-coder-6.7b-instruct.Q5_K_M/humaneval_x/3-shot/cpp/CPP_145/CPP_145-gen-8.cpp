    vector<pair<int,int>> nums_with_points;
    int i;
    for(i=0;i<nums.size();i++)
    {
        int sum=0;
        string num_str=to_string(abs(nums[i]));
        for(char c : num_str)
            sum+=c-'0';
        nums_with_points.push_back({nums[i],sum});
    }
    sort(nums_with_points.begin(),nums_with_points.end(),[](pair<int,int> a,pair<int,int> b){
        if(a.second==b.second)
            return a.first<b.first;
        return a.second<b.second;});
    vector<int> result;
    for(auto p : nums_with_points)
        result.push_back(p.first);
    return result;
}

