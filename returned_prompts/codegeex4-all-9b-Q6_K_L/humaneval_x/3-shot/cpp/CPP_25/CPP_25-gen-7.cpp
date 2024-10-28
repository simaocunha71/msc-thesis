    vector<int> factors;
    int i;
    for (i=2;i<=n;i++)
    {
        while (n%i==0){
            factors.push_back(i);
            n=n/i;
        }
    }
    return factors;
}

