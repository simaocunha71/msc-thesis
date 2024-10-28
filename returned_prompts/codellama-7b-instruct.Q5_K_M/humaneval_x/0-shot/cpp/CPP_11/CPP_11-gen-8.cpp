    int i;
    int j;
    int l;
    int m;
    int n;
    int x;
    int y;
    int z;
    l=a.length();
    m=b.length();
    n=max(l,m);
    z=0;
    for(i=0;i<l;i++)
    {
        x=a[i];
        y=b[i];
        if(x==y)
        {
            z=z+0;
        }
        else
        {
            z=z+1;
        }
    }
    if(l>m)
    {
        for(i=m;i<l;i++)
        {
            x=a[i];
            if(x==1)
            {
                z=z+1;
            }
            else
            {
                z=z+0;
            }
        }
    }
    else
    {
        for(i=l;i<m;i++)
        {
            y=b[i];
            if(y==1)
            {
                z=z+1;
            }
            else
            {
                z=z+0;
            }
        }
    }
    string s=to_string(z);
    return s;
}


