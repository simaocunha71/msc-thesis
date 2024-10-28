    vector<int> maxs;
    int i;
    int max=numbers[0];
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>max)
            max=numbers[i];
        maxs.push_back(max);
    }
    return maxs;
}

