    int product=1;
    int num=n;
    while(num>0)
    {
        int digit=num%10;
        if(digit%2!=0)
        product*=digit;
        num=num/10;
    }
    return product;
}