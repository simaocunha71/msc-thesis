    vector<int> maxes;
    int curr_max=numbers[0];
    int i;
    maxes.push_back(curr_max);
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>curr_max)
        {
        curr_max=numbers[i];
        }
        maxes.push_back(curr_max);
    }
    return maxes;
}



