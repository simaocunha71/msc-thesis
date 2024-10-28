    vector<int> maxes;
    int curr_max;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        curr_max=numbers[i];
        for (int j=i-1;j>=0;j--)
        {
            curr_max=max(numbers[j],curr_max);
        }
        maxes.push_back(curr_max);
    }
    return maxes;
}


