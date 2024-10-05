    vector<int> maxes;
    int max=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (max<numbers[i])
        {
            max=numbers[i];
        }
        maxes.push_back(max);
    }
    return maxes;
}


