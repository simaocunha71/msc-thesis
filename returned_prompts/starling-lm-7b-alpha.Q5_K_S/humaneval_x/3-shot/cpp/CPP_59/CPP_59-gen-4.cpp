    int i,res;
    for (i=2;i<=sqrt(n);i++)
    if (n%i==0)
    {
        res=i;
        while (n%i==0)
        {
            n/=i;
        }
        if (n==1)
        return res;
        else
        return largest_prime_factor(n);
    }
    return n;
}



