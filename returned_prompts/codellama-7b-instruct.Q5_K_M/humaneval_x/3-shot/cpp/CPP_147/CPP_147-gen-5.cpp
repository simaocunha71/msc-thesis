    int count=0;
    int i,j,k;
    vector<int> a(n);
    for (i=1;i<=n;i++)
    a[i-1]=i*i-i+1;
    for (i=0;i<n-1;i++)
    for (j=i+1;j<n-1;j++)
    for (k=j+1;k<n;k++)
    if (a[i]+a[j]+a[k]%3==0)
    count++;
    return count;
}


