    int ans=1;
    for (int i=0;i<n;i++)
    {
        ans*=2;
        ans%=p;
    }
    return ans;
}

