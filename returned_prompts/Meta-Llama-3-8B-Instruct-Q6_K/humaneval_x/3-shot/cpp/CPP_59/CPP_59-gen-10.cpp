    int i;
    for(i=n/2; i>1; i--)
    {
        if(n%i==0)
        {
            if(is_prime(i))
            return i;
        }
    }
    return 2;
}

bool is_prime(int n)
{
    if(n <= 1)
        return false;
    if(n == 2)
        return true;
    if(n % 2 == 0)
        return false;

    int i;
    for(i = 3; i * i <= n; i += 2)
    {
        if(n % i == 0)
            return false;
    }
    return true;
}