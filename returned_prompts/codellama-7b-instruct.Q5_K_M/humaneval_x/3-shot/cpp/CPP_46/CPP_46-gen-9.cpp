    int a=0,b=2,c=0,d=0,i;
    for (i=0;i<n;i++)
    {
        d=a+b+c;
        a=b;
        b=c;
        c=d;
    }
    return d;
}



