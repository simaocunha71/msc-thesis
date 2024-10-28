    int a=0;
    int b=2;
    int c=0;
    int d=0;
    int i;
    for (i=3;i<n;i++)
    {
        a=b;
        b=c;
        c=d;
        d=a+b+c;
    }
    return d;
}



