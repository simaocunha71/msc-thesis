    int product=1;
    int remainder;
    while(n>0)
    {
        remainder=n%10;
        if (remainder%2!=0)
        {
            product*=remainder;
        }
        n=n/10;
    }
    return product;
}