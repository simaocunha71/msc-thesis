    vector<int> factors;
    int i;
    for(i=2;i*i<=n;i++)
    {
        if(n%i==0)
        {
            int count=0;
            while(n%i==0)
            {
                n=n/i;
                count++;
            }
            factors.push_back(i);
            factors.insert(factors.end(),count,i);
        }
    }
    if(n>1)
    {
        factors.push_back(n);
    }
    return factors;
}