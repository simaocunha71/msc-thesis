    int i;
    for (i=n;i>1;i--)
    if (n%i==0 && is_prime(i)){
        return i;
    }
    return -1;
}

