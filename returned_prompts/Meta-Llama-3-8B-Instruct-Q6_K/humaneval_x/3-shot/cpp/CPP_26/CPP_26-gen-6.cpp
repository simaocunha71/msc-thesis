    vector<int> unique_numbers;
    for(int i=0; i<numbers.size(); i++)
    {
        bool is_unique = true;
        for(int j=0; j<unique_numbers.size(); j++)
        {
            if(unique_numbers[j] == numbers[i])
            {
                is_unique = false;
                break;
            }
        }
        if(is_unique)
        {
            unique_numbers.push_back(numbers[i]);
        }
    }
    return unique_numbers;
}

