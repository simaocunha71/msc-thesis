    int i;
    for (i=n/2;i>1;i--)
    {
        if (n%i==0)
        {
            if (is_prime(i))
            return i;
        }
    }
    return 2;
}

bool is_prime(int num)
{
    if(num <= 1)
        return false;
    if(num <= 3)
        return true;
    if(num%2 == 0 || num%3 == 0)
        return false;
    for(int i=5; i*i <= num; i=i+6)
        if(num%i == 0 || num%(i+2) == 0)
            return false;
    return true;
} 

