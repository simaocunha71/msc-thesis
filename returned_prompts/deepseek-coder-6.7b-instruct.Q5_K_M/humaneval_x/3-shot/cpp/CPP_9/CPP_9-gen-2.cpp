    vector<int> max_numbers;
    int max_number=numbers[0];
    max_numbers.push_back(max_number);
    for(int i=1;i<numbers.size();i++)
    {
        if(numbers[i]>max_number)
        {
            max_number=numbers[i];
        }
        max_numbers.push_back(max_number);
    }
    return max_numbers;
}


