    vector<int> maxes;
    int i;
    int max=numbers[0];
    maxes.push_back(max);
    for  (i=1;i<numbers.size();i++)
    {
        if  (numbers[i]>max)
        {
            max=numbers[i];
        }
        maxes.push_back(max);
    }
    return maxes;
}


