    if (n==2) return true;
    if (n<2 || n%2==0) return false;
    for (long long i=3;i<=sqrt(n);i++)
        if (n%i==0) return false;
    return true;
}


