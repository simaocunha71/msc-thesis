    int i,j;
    int fib[100];
    fib[0]=0;
    fib[1]=1;
    for (i=2;i<=n;i++)
    {
        fib[i]=fib[i-1]+fib[i-2];
    }
    for (i=0;i<=n;i++)
    {
        for (j=2;j<=fib[i]/2;j++)
        {
            if (fib[i]%j==0)
            {
                break;
            }
        }
        if (j>fib[i]/2)
        {
            return fib[i];
        }
    }
}

