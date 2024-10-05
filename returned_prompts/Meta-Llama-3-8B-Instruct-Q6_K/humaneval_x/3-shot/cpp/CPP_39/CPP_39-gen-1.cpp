    int a=0,b=1,c=0;
    for (int i=1;i<n;i++){
        a=b;
        b=c;
        c=a+b;
        if (is_prime(c))
        return c;
    }
}

bool is_prime(int num){
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;

    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}  // end of is_prime function
// end of prime_fib function
// end of code
// end of code
// end of code

