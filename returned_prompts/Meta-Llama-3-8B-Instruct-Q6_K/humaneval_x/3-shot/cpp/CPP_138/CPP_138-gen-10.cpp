    for (int i=2; i<=n; i+=2)
    {
        int sum=0;
        for (int j=2; j<=n; j+=2)
        {
            if (sum+i==n)
                return true;
            if (sum+i>n)
                return false;
            sum+=j;
        }
    }
    return false;
}
