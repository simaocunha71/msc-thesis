    vector<int> tri;
    tri.push_back(1);
    if (n>0) tri.push_back(3);
    if (n>1) tri.push_back(2);
    for (int i=3;i<=n;i++)
    {
        int sum=0;
        for (int j=1;j<=3;j++)
            if (i-j>=0)
                sum+=tri[i-j];
        tri.push_back(sum);
    }
    return tri;
}