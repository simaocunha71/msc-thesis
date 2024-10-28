    if (n==0||n==1||n==2)
    return 0;
    if (n==3)
    return 1;

    int a=0,b=0,c=1;
    for (int i=4;i<=n;i++)
    {
        a=b;
        b=c;
        c=a+b;
    }
    return c;
}


