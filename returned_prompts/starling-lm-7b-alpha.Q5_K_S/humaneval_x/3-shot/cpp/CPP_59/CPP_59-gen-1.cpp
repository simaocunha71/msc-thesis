    int i;
    for (i=2;i<=sqrt(n);i++)
    if (n%i==0)
    {
        if (isprime(i))
        return i;
        if (isprime(n/i))
        return n/i;
    }
    return n;
}

bool isprime(int n)
{
    int i;
    if (n==2||n==3)
    return true;
    if (n%2==0||n<2)
    return false;
    for (i=3;i<=sqrt(n);i++)
    if (n%i==0)
    return false;
    return true;
}



