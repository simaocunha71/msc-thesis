    if (n <= 1){
        return false;
    }
    if (n <= 3){
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0){
        return false;
    }

B:
    for (long long i = 5; i * i <= n; i += 6){
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}
int main() {
    long long n;
    printf("Enter a number: ");
    scanf("%lld", &n);
    if (is_prime(n)) {
        printf("%lld is a prime number\n", n);
    } else {
        printf("%lld is not a prime number\n", n);
    }
    return 0;
}

*/

#include<stdio.h>
bool is_prime(long long n){
    if (n <= 1){
        return false;
    }
    if (n <= 3){
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0){
        return false;
    }

    for (long long i = 5; i * i <= n; i += 6){
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}

int main() {
    long long n;
    printf("Enter a number: ");
    scanf("%lld", &n);
    if (is_prime(n)) {
        printf("%lld is a prime number\n", n);
    } else {
        printf("%lld is not a prime number\n", n);
    }
    return 0;
}
// End of Code


```

This is a simple C++ program that checks whether a given number is prime or not. 

The program starts with a function called `is_prime` that takes an argument `n` of type `long long`. 

In this function, a set of conditions checks if `n`