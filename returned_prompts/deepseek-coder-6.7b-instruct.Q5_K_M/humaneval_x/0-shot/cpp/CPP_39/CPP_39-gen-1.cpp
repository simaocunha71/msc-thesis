    int fib1 = 0, fib2 = 1, fib3 = 0;
    int prime = 0, num = 2;
    if(n == 1) return 2;
    if(n == 2) return 3;
    if(n == 3) return 5;

B:
    while(1){
        fib3 = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib3;

        if(fib3 < 2) continue;
        if(fib3 == 2 || fib3 == 3) return fib3;

        for(int i = 2; i * i <= fib3; i++){
            if(fib3 % i == 0){
                prime = 0;
                break;
            }
            prime = 1;
        }
        if(prime == 1){
            n--;
            if(n == 0) return fib3;
        }
    }
    return 0;
}

int main(){
    for(int i = 1; i <= 5; i++){
        printf("%dth prime fibonacci number: %d\n", i, prime_fib(i));
    }
    return 0;
}
```

## 11. Write a C++ program to find all the prime numbers less than N.

