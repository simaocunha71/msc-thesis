    int product=1;
    bool is_even=true;
    int i;
    while (n>0){
        if (n%2==1){
            product*=n;
            is_even=false;
        }
        n/=10;
    }
    if (is_even)
    return 0;
    else
    return product;
}