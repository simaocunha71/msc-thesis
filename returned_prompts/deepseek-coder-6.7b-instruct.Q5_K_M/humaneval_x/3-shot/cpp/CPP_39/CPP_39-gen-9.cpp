    int fib1 = 0;
    int fib2 = 1;
    int fib3 = 1;
    int i=1;
    int count=0;
    bool is_prime;

    while(count<n){
        if(fib3==2 || fib3==3){
            is_prime=true;
        }
        else if(fib3%2==0 || fib3%3==0){
            is_prime=false;
        }
        else{
            int j=1;
            while((j*j)<=fib3){
                if(fib3%j==0){
                    is_prime=false;
                    break;
                }
                j=j+2;
            }
            is_prime=true;
        }
        if(is_prime){
            count++;
        }
        if(count<n){
            fib1 = fib2;
            fib2 = fib3;
            fib3 = fib1 + fib2;
        }
    }
    return fib3;
}


