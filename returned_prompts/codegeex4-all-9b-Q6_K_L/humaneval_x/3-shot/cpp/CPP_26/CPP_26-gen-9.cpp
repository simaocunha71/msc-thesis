    vector<int> new_numbers;
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=0;j<new_numbers.size();j++)
    if (numbers[i]==new_numbers[j])
    break;
    if (j==new_numbers.size())
    new_numbers.push_back(numbers[i]);
    return new_numbers;
}

