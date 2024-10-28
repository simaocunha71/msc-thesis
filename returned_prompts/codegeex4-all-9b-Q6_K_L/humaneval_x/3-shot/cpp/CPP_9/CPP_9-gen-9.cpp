    vector<int> max_numbers;
    int max_element;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (i==0)
        {
            max_element=numbers[i];
            max_numbers.push_back(max_element);
        }
        else
        {
            if (numbers[i]>max_element)
            {
            max_element=numbers[i];
            }
            max_numbers.push_back(max_element);
        }
    }
    return max_numbers;
}

