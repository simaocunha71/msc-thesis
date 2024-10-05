    vector<int> new_numbers;
    for (int i=0;i<numbers.size();i++)
    {
        if (find(new_numbers.begin(), new_numbers.end(), numbers[i])==new_numbers.end())
        new_numbers.push_back(numbers[i]);
    }
    return new_numbers;
}

