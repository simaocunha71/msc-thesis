    int i;
    if (n%2==0)
    return x;
    for (i=3;i<=sqrt(n);i+=2)
    if (n%i==0)
    return y;
    return x;
}



