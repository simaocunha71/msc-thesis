    vector<int> a;
    int i;
    for (i=1;i<=n;i++)
    a.push_back(i*i-i+1);

    int count=0;
    for (i=0;i<n-2;i++)
    if (a[i]+a[i+1]+a[i+2]%3==0)
    count+=1;
    return count;
}

