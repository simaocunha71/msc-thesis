    if (n<2)
    return false;

    if (n==2)
    return true;

    if (n%2==0)
    return false;

    long long i;
    for (i=3;i<=sqrt(n);i+=2)
    if (n%i==0)
    return false;

    return true;
}



