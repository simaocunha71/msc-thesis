    int i;
    for (i=1;i<=min(a,b);i++)
    {
        if (a%i==0 && b%i==0)
        return i;
    }
    return 1;
}

