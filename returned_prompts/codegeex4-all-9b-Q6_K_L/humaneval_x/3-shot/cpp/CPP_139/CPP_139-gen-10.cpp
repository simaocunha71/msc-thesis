    long long ans=1;
    while (n>0)
    {
        for (int i=1;i<=n;i++)
        ans*=i;
        n-=1;
    }
    return ans;
}

