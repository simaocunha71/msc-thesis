    vector<pair<int,int>> sum_points;
    for(int i=0; i<nums.size(); i++)
    {
        int sum=0;
        int num = abs(nums[i]);
        while(num)
        {
            sum+=num%10;
            num/=10;
        }
        sum_points.push_back(make_pair(sum,nums[i]));
    }
    sort(sum_points.begin(), sum_points.end());
    vector<int> res;
    for(int i=0; i<sum_points.size(); i++)
    {
        res.push_back(sum_points[i].second);
    }
    return res;
}


