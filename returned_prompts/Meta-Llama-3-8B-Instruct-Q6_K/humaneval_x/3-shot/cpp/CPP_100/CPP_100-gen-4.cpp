    vector<int> pile;
    int level;
    for (level=1;level<=n;level++)
    {
        if (level%2==0)
        pile.push_back(level*2-1);
        else
        pile.push_back(level*2);
    }
    return pile;
}