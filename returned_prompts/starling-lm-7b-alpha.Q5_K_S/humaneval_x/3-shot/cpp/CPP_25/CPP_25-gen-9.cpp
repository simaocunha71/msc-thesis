    vector<int> factors;
    int i,j;
    for (i=2;i<=sqrt(n);i++)
    while (n%i==0)
    {
        factors.push_back(i);
        n/=i;
    }
    if (n>1)
    factors.push_back(n);
    return factors;
}


