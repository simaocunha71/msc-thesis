    vector<int> res(n);
    for (int i=1;i<n;i++)
    {
        if (i%2==0)
        res[i]=i;
        else
        res[i]=1+i;
    }
    return res;
}


