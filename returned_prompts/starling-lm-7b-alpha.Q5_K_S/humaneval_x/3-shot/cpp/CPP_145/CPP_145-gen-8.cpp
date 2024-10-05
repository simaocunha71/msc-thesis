    vector<int> all_nums;
    vector<int> all_nums_points;
    int i;
    int num;
    int sum;
    int j;
    for (i=0;i<nums.size();i++)
    {
        num=nums[i];
        sum=0;
        for (j=1;j<=num;j*=10)
        sum+=num/j;
        all_nums.push_back(num);
        all_nums_points.push_back(sum);
    }
    vector<int> ordered_nums;
    int min_points=10000000;
    for (i=0;i<all_nums_points.size();i++)
    if (all_nums_points[i]<min_points)
    {
        min_points=all_nums_points[i];
        ordered_nums.clear();
        ordered_nums.push_back(all_nums[i]);
    }
    else if (all_nums_points[i]==min_points)
    ordered_nums.push_back(all_nums[i]);
    return ordered_nums;
}



