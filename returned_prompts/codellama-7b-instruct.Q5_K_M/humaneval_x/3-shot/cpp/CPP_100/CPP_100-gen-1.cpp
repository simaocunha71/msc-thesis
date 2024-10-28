    vector<int> pile;
    int i;
    for (i=0;i<n;i++)
    {
        if ((n%2)==0)
        {
            pile.push_back(n);
            n++;
        }
        else
        {
            pile.push_back(n);
            n+=2;
        }
    }
    return pile;
}


