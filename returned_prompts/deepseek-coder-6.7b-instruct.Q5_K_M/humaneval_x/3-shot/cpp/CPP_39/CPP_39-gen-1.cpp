    int fib_n_minus_2 = 1;
    int fib_n_minus_1 = 2;
    int count = 1;
    while(count < n){
        int temp = fib_n_minus_1;
        fib_n_minus_1 += fib_n_minus_2;
        fib_n_minus_2 = temp;
        count++;
    }
    return fib_n_minus_2;
}

bool is_prime(int num){
    if(num <= 1)
        return false;
    if(num == 2)
        return true;
    if(num % 2 == 0)
        return false;
    for(int i = 3; i * i <= num; i += 2){
        if(num % i == 0)
            return false;
    }
    return true;
}

int prime_fib_v2(int n){
    int count = 0;
    int fib = 0;
    while(count < n){
        fib = prime_fib(++count);
        while(!is_prime(fib))
            fib = prime_fib(++count);
    }
    return fib;
}


