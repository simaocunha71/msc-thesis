    vector<int> pile;
    int odd_even=n%2;
    int next_odd=n+1;
    int next_even=n+2;
    if (odd_even==0)
    pile.push_back(next_even);
    else
    pile.push_back(next_odd);
    n=next_odd;
    while (n>1)
    {
    odd_even=n%2;
    next_odd=n+1;
    next_even=n+2;
    if (odd_even==0)
    pile.push_back(next_even);
    else
    pile.push_back(next_odd);
    n=next_odd;
    }
    return pile;
}


