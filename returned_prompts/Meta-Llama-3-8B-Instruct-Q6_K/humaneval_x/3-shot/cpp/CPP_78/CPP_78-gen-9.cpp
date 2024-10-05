    int count=0;
    for (int i=0; i<num.length(); i++)
    {
        if (num[i]>='2' && num[i]<='9')
        {
            if (isPrime(atoi(&num[i])))
            {
                count++;
            }
        }
        else if (num[i]>='A' && num[i]<='F')
        {
            if (isPrime(atoi(&num[i])-55))
            {
                count++;
            }
        }
    }
    return count;
}

bool isPrime(int n)
{
    if (n <= 1)
    {
        return false;
    }
    for (int i = 2; i < sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}