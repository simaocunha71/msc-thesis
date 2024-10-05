    for (int i=2; i<=n; i++)
    {
        int sum=0;
        for (int j=i; j<=n; j+=2)
        {
            sum+=j;
            if (sum==n)
                return true;
        }
    }
    return false;
}