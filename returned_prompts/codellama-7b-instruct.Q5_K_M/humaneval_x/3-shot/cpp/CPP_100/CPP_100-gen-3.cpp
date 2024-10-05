    vector<int> levels;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        levels.push_back(i+1);
        else
        levels.push_back(i+3);
    }
    return levels;
}



