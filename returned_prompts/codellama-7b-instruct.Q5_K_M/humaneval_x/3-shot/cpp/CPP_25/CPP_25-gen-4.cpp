    vector<int> factors;
    int factor,i;
    for (i=2;i<n;i++)
    if (n%i==0)
    {
        factor=i;
        while (n%factor==0){
            n/=factor;
            factors.push_back(factor);
        }
    }
    factors.push_back(n);
    return factors;
}


