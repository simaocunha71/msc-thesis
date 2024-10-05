    int i=2;
    int largest_factor=0;
    while (i*i<=n)
    {
        if (n%i==0)
        {
            n/=i;
            largest_factor=i;
        }
        else
        {
            i++;
        }
    }
    if (n>1)
    {
        largest_factor=n;
    }
    return largest_factor;
}


