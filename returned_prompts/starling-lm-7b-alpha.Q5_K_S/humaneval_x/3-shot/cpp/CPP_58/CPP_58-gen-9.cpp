    vector<int> all_nums;
    all_nums.insert(all_nums.end(),l1.begin(),l1.end());
    all_nums.insert(all_nums.end(),l2.begin(),l2.end());
    sort(all_nums.begin(),all_nums.end());
    int i;
    vector<int> unique_nums;
    unique_nums.push_back(all_nums[0]);
    for (i=1;i<all_nums.size();i++)
    if (all_nums[i]!=all_nums[i-1])
    unique_nums.push_back(all_nums[i]);

    vector<int> common_nums;
    for (i=0;i<unique_nums.size();i++)
    if (binary_search(l1.begin(),l1.end(),unique_nums[i]) && binary_search(l2.begin(),l2.end(),unique_nums[i]))
    common_nums.push_back(unique_nums[i]);
    sort(common_nums.begin(),common_nums.end());
    return common_nums;
}

