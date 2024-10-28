    vector<int> all_levels;
    for (int i=0;i<n;i++)
    {
        if (i%2==0)
        all_levels.push_back(i*2+3);
        else
        all_levels.push_back(i*2+2);
    }
    return all_levels;
}

