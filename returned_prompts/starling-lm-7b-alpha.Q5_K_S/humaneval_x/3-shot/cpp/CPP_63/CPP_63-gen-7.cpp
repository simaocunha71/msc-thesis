    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 1;
    if (n<4) return fibfib(n-1)+fibfib(n-2)+fibfib(n-3);
    int memo[4];
    memo[0]=0;
    memo[1]=0;
    memo[2]=1;
    memo[3]=1;
    for (int i=3;i<n;i++)
    {
        memo[i%4]=memo[(i-1)%4]+memo[(i-2)%4]+memo[(i-3)%4];
    }
    return memo[n%4];
}



