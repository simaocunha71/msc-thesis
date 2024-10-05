    vector<int> factors;
    int i,j;
    for (i=2;i<=n;i++)
    {
        j=0;
        while (n%i==0)
        {
            j+=1;
            n/=i;
        }
        if (j>0)
        factors.push_back(i);
    }
    return factors;
}


