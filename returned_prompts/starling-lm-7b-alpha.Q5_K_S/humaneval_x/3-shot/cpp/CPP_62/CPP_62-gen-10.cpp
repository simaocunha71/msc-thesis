    int i,j,n=xs.size();
    vector<float> ds(n-1,0);
    for (i=0;i<n-1;i++)
    {
        ds[i]=xs[i+1];
        if (i>0)
        ds[i]+=xs[i]*i;
    }
    return ds;
}



