    int count=0;
    int i,j,k;
    vector<int> a(n,0);
    for (i=1;i<=n;i++)
    a[i]=i*i-i+1;
    for (i=1;i<n;i++)
    for (j=i+1;j<n;j++)
    for (k=j+1;k<n;k++)
    if ((a[i]+a[j]+a[k])%3==0)
    count+=1;
    return count;
}


