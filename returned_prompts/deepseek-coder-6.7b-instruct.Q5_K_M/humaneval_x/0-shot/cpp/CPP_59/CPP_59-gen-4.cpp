    int i;
    for(i = 2; i*i <= n; i++){
        while(n % i == 0){
            n /= i;
        }
    }
    return n;
}

int main() {
    int n = 13195;
    printf("%d\n", largest_prime_factor(n));
    return 0;
}




*/

#include<stdio.h>

int largest_prime_factor(int n){
    int i;
    for(i = 2; i*i <= n; i++){
        while(n % i == 0){
            n /= i;
        }
    }
    return n;
}

int main() {
    int n = 13195;
    printf("%d\n", largest_prime_factor(n));
    return 0;
}
```

The code works by dividing the input number `n` by integers starting from 2 up to the square root of `n`. If `n` is divisible by the integer `i`, it divides `n` by `i` and continues the process until `n` is no longer divisible by `i`. The reason we only need to check up to the square root of `n` is that a larger factor of `n` would be a multiple of a smaller factor that has already been checked. The last factor found is the largest prime factor of `n`.

In the provided example, the largest prime factor of 13195 is 29, so the output of the program will be `29`.

Please note that the code uses integer division (`/`), which truncates the result to an integer. This means that if `n` is not divisible by `i`, `n / i` will be an integer. If `n` is divisible by `i`, `n / i` will be a floating point number, which is automatically converted to an integer by the compiler.

Also note that the `main` function is necessary for a C++ program to run. In this case, it calls the `largest_prime_factor` function with the argument `13195`, and prints the result