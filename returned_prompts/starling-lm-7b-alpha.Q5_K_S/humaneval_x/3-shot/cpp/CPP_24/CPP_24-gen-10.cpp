    int i=2,max_divisor=1;
    while (i<n)
    {
        if (n%i==0)
        {
            max_divisor=i;
        }
        i+=1;
    }
    return max_divisor;
}


