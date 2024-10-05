    sort(numbers.begin(),numbers.end());
    vector<int> new_numbers;
    int i;
    for (i=0;i<numbers.size()-1;i++)
    if (numbers[i]!=numbers[i+1])
    new_numbers.push_back(numbers[i]);
    if (numbers[numbers.size()-1]!=numbers[numbers.size()-2])
    new_numbers.push_back(numbers[numbers.size()-1]);
    return new_numbers;
}

