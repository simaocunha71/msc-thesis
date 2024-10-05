    vector<int> a;
    int i;
    int count=0;
    for (i=1;i<=n;i++)
    {
        a.push_back(i*i-i+1);
    }
    int j,k;
    for (i=0;i<n;i++)
    for (j=i+1;j<n;j++)
    for (k=j+1;k<n;k++)
        if ((a[i]+a[j]+a[k])%3==0)
        count+=1;

    return count;
}

