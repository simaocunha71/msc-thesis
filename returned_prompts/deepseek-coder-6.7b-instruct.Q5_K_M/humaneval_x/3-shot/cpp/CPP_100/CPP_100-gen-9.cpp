    vector<int> pile(n);
    int stones=n;
    for  (int i=0;i<n;i++)
    {
        pile[i]=stones;
        if (stones%2==0)
        stones+=2;
        else
        stones+=2;
    }
    return pile;
}


