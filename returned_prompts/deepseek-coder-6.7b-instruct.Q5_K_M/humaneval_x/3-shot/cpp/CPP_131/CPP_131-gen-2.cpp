    int product = 1;
    while(n){
        int digit = n % 10;
        if(digit % 2 != 0){
            product *= digit;
        }
        n = n / 10;
    }
    return product;
}


