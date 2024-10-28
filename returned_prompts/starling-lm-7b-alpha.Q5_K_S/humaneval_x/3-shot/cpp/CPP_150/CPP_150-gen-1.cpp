    if (n%2==0)
    return y;
    int i,limit=(int)sqrt(n);
    for (i=3;i<=limit;i++)
    if (n%i==0)
    return x;
    return y;
}


