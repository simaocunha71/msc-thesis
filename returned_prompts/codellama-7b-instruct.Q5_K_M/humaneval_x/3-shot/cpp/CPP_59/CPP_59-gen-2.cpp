    int i;
    for (i=n-1;i>1;i--)
    if (n%i==0 && is_prime(i))
    return i;
}


