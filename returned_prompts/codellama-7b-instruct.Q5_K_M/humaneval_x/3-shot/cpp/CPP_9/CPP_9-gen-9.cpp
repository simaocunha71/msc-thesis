    vector<int> max_numbers;
    int i;
    int max_number;
    max_number=numbers[0];
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]>max_number)
        max_number=numbers[i];
        max_numbers.push_back(max_number);
    }
    return max_numbers;
}



