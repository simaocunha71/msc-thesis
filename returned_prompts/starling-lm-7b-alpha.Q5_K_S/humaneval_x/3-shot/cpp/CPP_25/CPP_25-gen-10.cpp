    vector<int> factors;
    int i,limit;
    int root=sqrt(n);
    for (i=2;i<=root;i++)
    {
        if (n%i==0)
        {
            factors.push_back(i);
            while (n%i==0)
            n/=i;
        }
    }
    if (n>1)
    factors.push_back(n);

    return factors;
}


