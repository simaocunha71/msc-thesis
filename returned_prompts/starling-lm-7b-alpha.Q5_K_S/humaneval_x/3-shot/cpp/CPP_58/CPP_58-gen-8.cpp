    vector<int> common_nums;
    int i;
    for (i=0;i<l1.size();i++)
    if (binary_search(l2.begin(),l2.end(),l1[i]))
    {
        if (!binary_search(common_nums.begin(),common_nums.end(),l1[i]))
        common_nums.push_back(l1[i]);
    }
    sort(common_nums.begin(),common_nums.end());
    return common_nums;
}



