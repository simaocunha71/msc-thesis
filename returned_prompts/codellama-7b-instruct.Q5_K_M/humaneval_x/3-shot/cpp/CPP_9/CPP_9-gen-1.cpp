    vector<int> maxes;
    int max=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++)
    {
        max=numbers[i];
        for (int j=i;j<numbers.size();j++)
        {
            if (numbers[j]>max)
                max=numbers[j];
        }
        maxes.push_back(max);
    }
    return maxes;
}


