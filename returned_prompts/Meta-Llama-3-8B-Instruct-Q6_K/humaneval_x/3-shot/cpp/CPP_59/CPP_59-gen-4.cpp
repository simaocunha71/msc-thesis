    int i;
    for(i=n/2;i>1;i--)
    {
        if(n%i==0)
        {
            if(is_prime(i))
            {
                return i;
            }
        }
    }
    return 2;
}

bool is_prime(int n)
{
    int i;
    for(i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
        {
            return false;
        }
    }
    return true;
}   


