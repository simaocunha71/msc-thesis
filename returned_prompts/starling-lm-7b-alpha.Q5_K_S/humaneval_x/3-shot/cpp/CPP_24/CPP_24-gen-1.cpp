    int i,max_divisor=0;
    for (i=2;i<n;i++)
    {
        if (n%i==0)
            max_divisor=i;
    }
    return max_divisor;
}


