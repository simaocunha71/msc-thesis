    int i,f1=0,f2=1,f3=1;
    while (f3<n)
    {
        f3=f1+f2;
        f1=f2;
        f2=f3;
    }
    for (i=2;i<=f3/2;i++)
    if (f3%i==0)
    return 0;

    return 1;
}


