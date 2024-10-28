    int a=0, b=0, c=2, d=0, i;
    if (n==0||n==1||n==2||n==3)
    return a;
    for (i=0;i<n;i++)
    {
        d=c;
        c=a+b+c;
        a=b;
        b=d;
    }
    return c;
}


