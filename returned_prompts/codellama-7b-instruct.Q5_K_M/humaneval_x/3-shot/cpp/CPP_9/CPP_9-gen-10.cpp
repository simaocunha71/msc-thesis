    vector<int> maxs;
    int max_so_far=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        max_so_far=max(max_so_far, numbers[i]);
        maxs.push_back(max_so_far);
    }
    return maxs;
}


