    vector<int> stones;
    int stones_on_level=0;
    int i;
    for (i=1;i<=n;i++)
    {
        if (n%2==0)
            stones_on_level+=2*i;
        else
            stones_on_level+=2*i-1;
        stones.push_back(stones_on_level);
    }
    return stones;
}

