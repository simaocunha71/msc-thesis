    int product=1;
    while(n){
        if((n%10)%2==1){
            product*=n%10;
        }
        n/=10;
    }
    return product;
}


