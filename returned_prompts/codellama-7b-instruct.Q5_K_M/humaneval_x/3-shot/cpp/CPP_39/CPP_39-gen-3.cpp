    int a=0;
    int b=1;
    int c=0;
    int d=1;
    int i;
    for (i=0;i<n;i++)
    {
        c=a+b;
        a=b;
        b=c;
        d=a+b;
        a=b;
        b=d;
        if (is_prime(d))
        return d;
    }
    return d;
}


