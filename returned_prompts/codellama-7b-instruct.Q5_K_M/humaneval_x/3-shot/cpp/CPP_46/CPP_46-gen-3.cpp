    int a=0,b=0,c=2,d=0;
    for (int i=0;i<n;i++)
    {
        a=b;
        b=c;
        c=d;
        d=a+b+c+d;
    }
    return d;
}


