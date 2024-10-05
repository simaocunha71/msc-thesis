    vector<int> maxs;
    maxs.push_back(numbers[0]);
    int i;
    for (i=1;i<numbers.size();i++)
    if (numbers[i]>maxs[i-1])
    maxs.push_back(numbers[i]);
    return maxs;
}


