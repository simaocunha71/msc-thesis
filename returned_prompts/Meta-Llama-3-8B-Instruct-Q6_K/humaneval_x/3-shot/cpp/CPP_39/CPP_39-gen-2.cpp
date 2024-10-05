    int a=0,b=1;
    int count=0;
    while(count<n)
    {
        int temp=a+a+b;
        if (is_prime(temp))
        {
            a=b;
            b=temp;
            count+=1;
        }
        else
        {
            b=temp;
        }
    }
    return b;
}

bool is_prime(int num)
{
    if (num <= 1)
        return false;
    for (int i = 2; i*i <= num; i++)
        if (num % i == 0)
            return false;
    return true;
} 