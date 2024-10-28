    vector<int> new_numbers;
    int i;

    for (i=0;i<numbers.size();i++)
    {
        new_numbers.push_back(numbers[i]);
        new_numbers.push_back(delimeter);
    }
    new_numbers.pop_back();
    return new_numbers;
}

