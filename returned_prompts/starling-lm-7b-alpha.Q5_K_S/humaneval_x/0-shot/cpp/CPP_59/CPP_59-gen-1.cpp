    if(n%2==0)
        return 2;
    for(int i=3;i*i<=n;i++)
        if(n%i==0)
            return i;
    return n;
}




/*
Return the largest prime factor of n. Assume n > 1 and is not a prime.