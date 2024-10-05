    vector<int> pile;
    int i=1;
    pile.push_back(n);
    while (n>1)
    {
        if (n%2==0)
        {
            n=n/2;
            pile.push_back(n);
        }
        else
        {
            n=n+1;
            pile.push_back(n);
        }
    }
    return pile;
}