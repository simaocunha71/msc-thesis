    if (n==1||n==0)
    return false;
    if (n==2||n==3)
    return true;
    for (long long i=2;i<n/2;i++)
    if (n%i==0)
    return false;
    return true;
}


