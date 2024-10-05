    int a=0;
    int b=1;
    int c=0;
    int i;
    for (i=0;i<n;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }
    for (i=2;i<c;i++)
    {
        if (c%i==0)
        return i;
    }
}


