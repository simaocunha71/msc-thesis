    vector<int> collatz_seq;
    if (n==1)
    return collatz_seq;
    else
    {
    collatz_seq.push_back(n);
    while (n!=1)
    {
        if (n%2==0)
        n/=2;
        else
        n=3*n+1;
        collatz_seq.push_back(n);
    }
    sort(collatz_seq.begin(),collatz_seq.end());
    return collatz_seq;
    }
}


