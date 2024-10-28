    vector<int> max_values;
    int current_max=numbers[0];
    int i;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]>current_max)
        {
            current_max=numbers[i];
        }
        max_values.push_back(current_max);
    }
    return max_values;
}

