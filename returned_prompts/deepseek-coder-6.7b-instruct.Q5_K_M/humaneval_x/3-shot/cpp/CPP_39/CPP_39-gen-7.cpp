    int fib_1=1,fib_2=1,fib_n=1,count=2;
    while(count<n){
        fib_n=fib_1+fib_2;
        fib_1=fib_2;
        fib_2=fib_n;
        if (is_prime(fib_n))
        count++;
    }
    return fib_n;
}
bool is_prime(int n){
    for(int i=2;i*i<=n;i++){
        if(n%i==0)
        return false;
    }
    return n>1;
}

