    vector<int> levels;
    int stones;
    for (int i=0;i<n;i++)
    {
        stones=0;
        if (n%2==0)
        stones=n+1;
        else
        stones=n+2;
        levels.push_back(stones);
        n=stones;
    }
    return levels;
}



