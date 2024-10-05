    int i;
    if (n%2==0 || n<2)
    return y;
    for (i=3;i<n;i++)
    if (n%i==0)
    return y;
    return x;
}



