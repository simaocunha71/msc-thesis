    vector<int> factors;
    int i;
    int d=2;
    while (d*d<=n)
    {
        if (n%d==0)
        {
            factors.push_back(d);
            while (n%d==0)
                n/=d;
        }
        d+=1;
    }
    if (n>1)
        factors.push_back(n);
    return factors;
}


