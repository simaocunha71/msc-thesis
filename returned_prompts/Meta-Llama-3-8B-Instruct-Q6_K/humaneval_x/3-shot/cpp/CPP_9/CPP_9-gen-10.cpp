    vector<int> maxs;
    int i;
    maxs.push_back(numbers[0]);
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>maxs[i-1])
        maxs.push_back(numbers[i]);
        else
        maxs.push_back(maxs[i-1]);
    }
    return maxs;
}