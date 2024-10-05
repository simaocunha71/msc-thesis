    vector<int> a(n);
    int sum, count=0;
    for (int i=1;i<=n;i++)
    {
        a[i-1]=i*i-i+1;
    }
    for (int i=0;i<n-2;i++)
    {
        for (int j=i+1;j<n-1;j++)
        {
            for (int k=j+1;k<n;k++)
            {
                sum=a[i]+a[j]+a[k];
                if (sum%3==0)
                {
                    count++;
                }
            }
        }
    }
    return count;
}