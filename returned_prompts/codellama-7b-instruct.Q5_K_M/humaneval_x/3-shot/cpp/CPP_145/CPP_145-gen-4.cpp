    vector<pair<int,int> > vec;
    int i;
    for (i=0;i<nums.size();i++)
    {
        int sum=0;
        while (nums[i])
        {
            sum+=nums[i]%10;
            nums[i]/=10;
        }
        vec.push_back({sum,i});
    }
    sort(vec.begin(),vec.end(),[](pair<int,int>& a,pair<int,int>& b){
        if (a.first==b.first)
        {
            return a.second<b.second;
        }
        return a.first<b.first;
    });
    vector<int> res;
    for (i=0;i<vec.size();i++)
    res.push_back(nums[vec[i].second]);
    return res;
}



