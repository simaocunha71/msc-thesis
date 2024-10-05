    vector<int> new_numbers;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        new_numbers.push_back(numbers[i]);
        if (i!=numbers.size()-1)
        new_numbers.push_back(delimeter);
    }
    return new_numbers;
}


