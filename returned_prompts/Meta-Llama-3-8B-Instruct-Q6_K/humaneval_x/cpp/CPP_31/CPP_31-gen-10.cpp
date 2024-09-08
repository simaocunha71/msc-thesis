    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6)); // false
    printf("%d\n", is_prime(101)); // true
    printf("%d\n", is_prime(11)); // true
    printf("%d\n", is_prime(13441)); // true
    printf("%d\n", is_prime(61)); // true
    printf("%d\n", is_prime(4)); // false
    printf("%d\n", is_prime(1)); // false
    return 0;
}

B:
```
Here is the C++ code to solve the problem. The `is_prime` function checks if a given number is prime or not. It returns `true` if the number is prime and `false` otherwise.

```c
#include <iostream>
using namespace std;

bool is_prime(long long n) {
    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6)); // false
    printf("%d\n", is_prime(101)); // true
    printf("%d\n", is_prime(11)); // true
    printf("%d\n", is_prime(13441)); // true
    printf("%d\n", is_prime(61)); // true
    printf("%d\n", is_prime(4)); // false
    printf("%d\n", is_prime(1)); // false
    return 0;
}
```

The `is_prime` function works by checking if the given number `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, it is not a prime number, so the function returns `false`. If `n` is not divisible by any of these numbers, it is a prime number, so the function returns `true`.

In the `main` function, we test the `is_prime` function with different numbers and print the results. The numbers are chosen to demonstrate the function's correctness. For example, 