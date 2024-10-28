    int fib=1;
    int fib2=1;
    int fib3;
    int i,j;
    if (n==1)
    return 2;
    if (n==2)
    return 3;
    for (i=3;i<=n;i++)
    {
        fib3=fib+fib2;
        fib=fib2;
        fib2=fib3;
        for (j=2;j<=fib3/2;j++)
        {
            if (fib3%j==0)
            break;
        }
        if (j>fib3/2)
        return fib3;
    }

}

