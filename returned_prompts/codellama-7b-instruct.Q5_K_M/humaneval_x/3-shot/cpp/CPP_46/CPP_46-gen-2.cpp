    int a=0, b=0, c=2, d=0;
    int i;
    for (i=0;i<n;i++)
    {
        d=a+b+c+d;
        a=b;
        b=c;
        c=d;
    }
    return d;
}


