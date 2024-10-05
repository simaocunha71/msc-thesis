    vector<int> all_nums;
    int i;
    for (i=0;i<numbers.size();i++)
    if (find(all_nums.begin(),all_nums.end(),numbers[i])==all_nums.end())
    all_nums.push_back(numbers[i]);
    return all_nums;
}


