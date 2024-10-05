    int i,limit=sqrt(n);
    for (i=limit;i>=2;i--)
    if (n%i==0 && is_prime(i))
    return i;
    return -1;
}



