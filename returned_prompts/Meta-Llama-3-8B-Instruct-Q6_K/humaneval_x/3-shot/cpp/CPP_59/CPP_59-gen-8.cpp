    int i;
    for (i=n/2;i>1;i--)
    {
        if (n%i==0)
        {
            if (is_prime(i))
            return i;
        }
    }
    return 2; // Default return, as 2 is the smallest prime number
}

bool is_prime(int i)
{
    int j;
    if (i<2)
        return false;
    for (j=2;j<i;j++)
        if (i%j==0)
            return false;
    return true;
}