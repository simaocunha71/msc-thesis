    vector<int> stones;
    if(n==1)
    {
        stones.push_back(1);
        return stones;
    }
    stones.push_back(n);
    int i=1;
    while(n>1)
    {
        if(n%2==0)
        {
            n=n/2;
            stones.push_back(n);
        }
        else
        {
            n=n-1;
            stones.push_back(n);
        }
    }
    return stones;
}

