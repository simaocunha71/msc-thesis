    vector<int> pile;
    int i;
    pile.push_back(n);
    for (i=1;i<n;i++)
    {
        if (i%2==0)
        pile.push_back(i*2+1);
        else
        pile.push_back(i*2);
    }
    return pile;
}