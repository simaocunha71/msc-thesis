    int product=1;
    while(n>0)
    {
        int digit=n%10;
        if(digit%2==1)
        product*=digit;
        n/=10;
    }
    return product;
}


