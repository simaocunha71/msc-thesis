    vector<int> factors;
    for (int i=1;i<=n;i++)
    if (n%i==0)
    {
        factors.push_back(i);
        n/=i;
    }
    return factors;
}


