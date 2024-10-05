    vector<int> factors;
    int i;
    for (i=2;i<=sqrt(n);i++)
    if (n%i==0)
    {
        factors.push_back(i);
        n/=i;
        i--;
    }
    if (n>2)
    factors.push_back(n);
    return factors;
}

