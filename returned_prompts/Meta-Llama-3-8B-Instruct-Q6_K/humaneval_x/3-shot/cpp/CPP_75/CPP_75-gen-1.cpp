    int i;
    bool is_prime[100];
    for (i=0;i<100;i++)
    is_prime[i]=true;

    for (i=2;i*i<=100;i++)
    {
        if (is_prime[i])
        {
        for (int j=i*i;j<=100;j+=i)
        is_prime[j]=false;
        }
    }
    for (i=2;i<=a;i++)
    if (is_prime[i] && a%i==0)
    {
        for (int j=i;j<=a;j+=i)
        {
            if (is_prime[j] && a/j==i)
            {
                for (int k=j;j*a<=100;j+=i)
                if (is_prime[k] && j*a/k==i)
                return true;
            }
        }
    }
    return false;
}