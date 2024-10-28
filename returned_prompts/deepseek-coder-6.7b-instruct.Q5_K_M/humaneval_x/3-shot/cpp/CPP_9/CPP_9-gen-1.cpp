    int i;
    vector<int> max_numbers;
    int max=numbers[0];
    for(i=0; i<numbers.size(); i++)
    {
        if(numbers[i]>max)
        {
            max=numbers[i];
        }
        max_numbers.push_back(max);
    }
    return max_numbers;
}

