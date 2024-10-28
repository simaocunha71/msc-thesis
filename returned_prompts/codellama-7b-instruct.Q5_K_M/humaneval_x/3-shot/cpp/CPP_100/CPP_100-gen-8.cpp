    vector<int> all_levels;
    int i;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        all_levels.push_back(i+1);
        if (i%2!=0)
        all_levels.push_back(i+2);
    }
    return all_levels;
}


