    int count=0;
    int i,j,k;
    int val;
    vector<int> a;
    for (i=1;i<=n;i++)
    a.push_back(i*i-i+1);
    for (i=0;i<a.size();i++)
    for (j=i+1;j<a.size();j++)
    for (k=j+1;k<a.size();k++)
    if (a[i]+a[j]+a[k]%3==0)
    count++;
    return count;
}



