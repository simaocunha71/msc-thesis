    vector<int> result;
    int max=INT_MIN;
    result.push_back(max);
    for(int i=1;i<numbers.size();i++)
    {
        max=max<numbers[i]?numbers[i]:max;
        result.push_back(max);
    }
    return result;
}