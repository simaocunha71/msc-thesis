    int i;
    for (i=n;i>=2;i--)
    if (n%i==0 && is_prime(i))
    return i;
}


