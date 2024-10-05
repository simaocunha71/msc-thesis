    vector<int> all_numbers;
    all_numbers.push_back(numbers[0]);
    int i;
    for (i=1;i<numbers.size();i++)
    {
        all_numbers.push_back(delimeter);
        all_numbers.push_back(numbers[i]);
    }
    return all_numbers;
}


