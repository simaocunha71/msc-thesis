    int digit;
    int product=1;
    while (n>0)
    {
        digit=n%10;
        if (digit%2==1)
        product*=digit;
        n=n/10;
    }
    if (product==1)
    return 0;
    else
    return product;
}

