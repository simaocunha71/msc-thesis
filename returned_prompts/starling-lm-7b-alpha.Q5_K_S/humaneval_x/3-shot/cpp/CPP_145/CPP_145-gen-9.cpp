    vector<int> all_nums;
    vector<int> all_points;
    int i,j;
    int point;
    int num;
    for (i=0;i<nums.size();i++)
    {
        point=0;
        num=nums[i];
        while (num>0)
        {
            point+=num%10;
            num/=10;
        }
        all_nums.push_back(point);
        all_points.push_back(i);
    }

    vector<pair<int, int>> all_nums_points;
    for (i=0;i<all_nums.size();i++)
    {
        all_nums_points.push_back({all_nums[i],all_points[i]});
    }
    sort(all_nums_points.begin(), all_nums_points.end());
    vector<int> result;
    for (i=0;i<all_nums_points.size();i++)
    {
        result.push_back(nums[all_nums_points[i].second]);
    }
    return result;
}


