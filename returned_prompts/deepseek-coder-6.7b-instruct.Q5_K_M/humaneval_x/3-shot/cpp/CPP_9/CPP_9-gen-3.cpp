    vector<int> max_numbers;
    int max_value=numbers[0];
    int i;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]>max_value)
        {
            max_value=numbers[i];
        }
        max_numbers.push_back(max_value);
    }
    return max_numbers;
}

