    int a=0,b=1,c=0;
    int i;
    for (i=1;i<n;i++)
    {
        c=a+b;
        a=b;
        b=c;
        if (is_prime(c))
        return c;
    }
    return -1;
}
bool is_prime(int number){
    if (number<2)
    return 0;
    int i;
    for (i=2;i<=sqrt(number);i++)
    if (number%i==0)
    return 0;
    return 1;
}