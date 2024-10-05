    vector<int> max_elements;
    int max_element=numbers[0];
    max_elements.push_back(max_element);
    for (int i=0;i<numbers.size();i++)
    {
        if (numbers[i]>=max_element)
        {
            max_element=numbers[i];
        }
        max_elements.push_back(max_element);
    }
    return max_elements;
}

