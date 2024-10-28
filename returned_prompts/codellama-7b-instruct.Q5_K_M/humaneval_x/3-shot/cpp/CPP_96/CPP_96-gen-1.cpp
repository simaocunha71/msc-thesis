    int i;
    if (n==2)
    return true;
    if (n%2==0)
    return false;
    for (i=3;i<n;i+=2)
    if (n%i==0)
    return false;
    return true;
}


