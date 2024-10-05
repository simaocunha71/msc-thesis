    vector<int> all_factors;
    int i,j;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        {
        int factorial=1;
        for (j=1;j<=i;j++)
        factorial*=j;
        all_factors.push_back(factorial);
        }
        else
        {
        int sum=0;
        for (j=1;j<=i;j++)
        sum+=j;
        all_factors.push_back(sum);
        }
    }
    return all_factors;
}



