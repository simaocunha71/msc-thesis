    vector<int> collatz;
    int i;
    collatz.push_back(n);
    while (n!=1)
    {
        if (n%2==1)
        {
            collatz.push_back(n);
        }
        if (n%2==0)
        {
            n=n/2;
        }
        else
        {
            n=3*n+1;
        }
    }

    sort(collatz.begin(),collatz.end());
    return collatz;
}

