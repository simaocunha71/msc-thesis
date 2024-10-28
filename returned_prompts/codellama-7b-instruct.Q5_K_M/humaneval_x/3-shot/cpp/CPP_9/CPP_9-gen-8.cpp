    vector<int> max_nums;
    int max_val=numbers[0];
    for (int i=0;i<numbers.size();i++)
    {
        max_val=max(numbers[i],max_val);
        max_nums.push_back(max_val);
    }
    return max_nums;
}


