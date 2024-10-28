    vector<string> nums = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<int> sorted;
    vector<string> result;
    for(auto &i: arr)
        if(i>=1 && i<=9) sorted.push_back(i);
    sort(sorted.begin(), sorted.end());
    reverse(sorted.begin(), sorted.end());
    for(auto &i: sorted)
        result.push_back(nums[i]);
    return result;
}


