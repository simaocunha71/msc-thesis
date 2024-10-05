    vector<int> new_nums;
    for (int i=0;i<numbers.size();i++)
    {
        new_nums.push_back(numbers[i]);
        new_nums.push_back(delimeter);
    }
    new_nums.pop_back();
    return new_nums;
}

