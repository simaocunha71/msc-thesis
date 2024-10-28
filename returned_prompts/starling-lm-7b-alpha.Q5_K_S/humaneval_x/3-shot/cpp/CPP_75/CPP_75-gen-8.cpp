    int i,n=a;
    for (i=2;i<=sqrt(n);i++)
    if (n%i==0)
    return false;
    return true;
}



