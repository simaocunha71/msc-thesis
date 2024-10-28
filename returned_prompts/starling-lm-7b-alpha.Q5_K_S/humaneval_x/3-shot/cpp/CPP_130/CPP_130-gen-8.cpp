    vector<int> all_tri;
    int i;
    int a=3;
    int b=1;
    int c=2;
    all_tri.push_back(a);
    all_tri.push_back(b);
    all_tri.push_back(c);
    for (i=3;i<=n;i++)
    {
        if (i%2==0)
        {
        a=all_tri[i-1];
        b=all_tri[i-2];
        c=all_tri[i-3];
        all_tri.push_back(1+i/2);
        }
        if (i%2==1)
        {
        a=all_tri[i-1];
        b=all_tri[i-2];
        c=all_tri[i-3];
        all_tri.push_back(a+b+c);
        }
    }
    return all_tri;
}


