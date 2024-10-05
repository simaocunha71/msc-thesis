    vector<int> all_nums;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        all_nums.push_back(numbers[i]);
        if (i<numbers.size()-1)
        all_nums.push_back(delimeter);
    }
    return all_nums;
}



