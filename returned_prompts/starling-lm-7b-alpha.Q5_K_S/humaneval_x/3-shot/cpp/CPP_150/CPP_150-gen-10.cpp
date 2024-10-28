    int i;
    if (n==2 || n==1) return y;
    for (i=2;i<n;i++)
    if (n%i==0) return x;
    return y;
}


