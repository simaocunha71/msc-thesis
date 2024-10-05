    int fibfib_n[n+1];
    fibfib_n[0]=0;
    fibfib_n[1]=0;
    fibfib_n[2]=1;
    int i;
    for (i=3;i<=n;i++)
    {
        fibfib_n[i]=fibfib_n[i-1]+fibfib_n[i-2]+fibfib_n[i-3];
    }
    return fibfib_n[n];
}

