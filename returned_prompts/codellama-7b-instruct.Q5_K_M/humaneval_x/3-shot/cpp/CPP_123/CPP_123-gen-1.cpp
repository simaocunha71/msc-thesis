    vector<int> odds;
    int current=n;
    while (current!=1)
    {
        if (current%2==1)
        odds.push_back(current);
        if (current%2==0)
        current=current/2;
        if (current%2!=0)
        current=3*current+1;
    }
    sort(odds.begin(), odds.end());
    return odds;
}

