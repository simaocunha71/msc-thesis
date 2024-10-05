    int i,j;
    vector<int> a(n);
    for (i=0;i<n;i++)
    {
        a[i]=i*i-i+1;
    }
    int count=0;
    for (i=0;i<n;i++)
    for (j=i+1;j<n;j++)
    for (;j<n;j++)
    if ((a[i]+a[j]+a[j])%3==0)
    count+=1;
    return count;
}


