    int i;
    int sum=0;
    for (i=2;i<=n/2;i+=2)
    if (n%i==0)
    sum+=i;
    if (sum==n)
    return true;
    return false;
}


