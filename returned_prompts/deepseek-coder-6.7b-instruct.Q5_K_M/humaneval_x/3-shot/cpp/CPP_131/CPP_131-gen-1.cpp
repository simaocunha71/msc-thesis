    int product=1;
    int digit;
    while(n>0){
        digit=n%10;
        if  (digit%2 != 0)
            product*=digit;
        n=n/10;
    }
    return product;
}



