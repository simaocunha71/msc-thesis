    vector<int> result;
    int i;
    int factorial;
    for (i=1;i<=n;i++)
    {
    if (i%2==0)
    {
        factorial=1;
        for (int j=1;j<=i;j++)
        factorial*=j;
        result.push_back(factorial);
    }
    else
    {
        int sum=0;
        for (int j=1;j<=i;j++)
        sum+=j;
        result.push_back(sum);
    }
    }
    return result;
}


