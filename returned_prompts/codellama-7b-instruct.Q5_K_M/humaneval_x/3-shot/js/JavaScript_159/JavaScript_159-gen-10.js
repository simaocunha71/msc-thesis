    vector<int> factors;
    for (int i=2;i<=sqrt(n);i++)
    {
        if (n%i==0)
        {
            factors.push_back(i);
            n=n/i;
            i=2;
        }
    }
    factors.push_back(n);
    return factors;
}


