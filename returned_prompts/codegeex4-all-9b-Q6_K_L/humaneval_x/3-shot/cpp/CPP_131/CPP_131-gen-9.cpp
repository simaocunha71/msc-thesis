    int product=1;
    int number=n;
    int digit;
    while (number!=0)
    {
        digit=number%10;
        if (digit%2==0)
        {
            return 0;
        }
        else
        {
            product*=digit;
        }
        number=number/10;
    }
    return product;
}

