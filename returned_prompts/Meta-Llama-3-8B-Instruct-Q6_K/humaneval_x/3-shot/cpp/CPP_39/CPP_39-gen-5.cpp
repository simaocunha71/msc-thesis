    int a=0,b=1,f=1;
    while(f<n){
        int temp=a+b;
        a=b;
        b=temp;
        if (is_prime(temp))
            f++;
    }
    return b;
}

bool is_prime(int num){
    if (num<2)
        return false;
    for (int i=2;i<=sqrt(num);i++)
        if (num%i==0)
            return false;
    return true;
}
// You can use the above function to check if a number is prime.
// The is_prime function is a helper function for the prime_fib function.


