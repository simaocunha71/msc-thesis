    vector<int> pile;
    pile.push_back(n);
    int current=n;
    while (n>1)
    {
        if (n%2==1)
        {
            n=n+1;
        }
        else
        {
            n=n+2;
        }
        pile.push_back(n);
    }
    return pile;
}