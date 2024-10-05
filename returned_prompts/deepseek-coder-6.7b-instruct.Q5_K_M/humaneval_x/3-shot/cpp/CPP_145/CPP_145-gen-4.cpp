    vector<pair<int,int>> vec;
    for(int i=0;i<nums.size();i++){
        int sum = 0;
        string num = to_string(abs(nums[i]));
        for(int j=0;j<num.size();j++){
            sum+=num[j]-'0';
        }
        vec.push_back(make_pair(sum,nums[i]));
    }
    sort(vec.begin(),vec.end());
    vector<int> res;
    for(int i=0;i<vec.size();i++){
        res.push_back(vec[i].second);
    }
    return res;
}

