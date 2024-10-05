    int i;
    vector<int> new_numbers;
    for (i=0;i<numbers.size();i++)
    if (i==numbers.size()-1)
    new_numbers.push_back(numbers[i]);
    else
    {
    new_numbers.push_back(numbers[i]);
    new_numbers.push_back(delimeter);
    }
    return new_numbers;
}

