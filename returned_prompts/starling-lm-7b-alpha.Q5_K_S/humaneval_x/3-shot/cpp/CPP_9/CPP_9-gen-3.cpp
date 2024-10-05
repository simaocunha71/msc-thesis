    vector<int> maxes;
    int max_number=INT_MIN;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        max_number=max(max_number,numbers[i]);
        maxes.push_back(max_number);
    }
    return maxes;
}


