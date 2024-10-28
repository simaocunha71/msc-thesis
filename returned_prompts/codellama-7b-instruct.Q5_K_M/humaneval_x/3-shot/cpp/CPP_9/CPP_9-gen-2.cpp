    vector<int> max_numbers;
    int max_val=numbers[0];
    for (int i=1;i<numbers.size();i++)
    {
        if (numbers[i]>max_val)
        {
            max_val=numbers[i];
        }
        max_numbers.push_back(max_val);
    }
    return max_numbers;
}


