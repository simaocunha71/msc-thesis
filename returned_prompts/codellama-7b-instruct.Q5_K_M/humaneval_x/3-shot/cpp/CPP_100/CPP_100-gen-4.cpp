    vector<int> pile;
    for (int i=0;i<n;i++)
    {
        int stones;
        if (n%2==0)
        stones=n+1;
        else
        stones=n+1;
        pile.push_back(stones);
        n=stones;
    }
    return pile;
}


