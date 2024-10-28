    int fibfib_a=0,fibfib_b=0,fibfib_c=1,i;
    if (n==0||n==1||n==2)
    return fibfib_a;
    for (i=3;i<=n;i++)
    {
        fibfib_c=fibfib_a+fibfib_b;
        fibfib_a=fibfib_b;
        fibfib_b=fibfib_c;
    }
    return fibfib_c;
}


