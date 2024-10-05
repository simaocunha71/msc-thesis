    int a,b;
    int i;
    a=0;
    b=1;
    for (i=1;i<n;i++)
    {
        int c=a+b;
        a=b;
        b=c;
        if (is_prime(c))
        return c;
    }
}


