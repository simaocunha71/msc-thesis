    int n = str.length();
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main()
{
    printf("%d\n",prime_length("Hello"));
    printf("%d\n",prime_length("abcdcba"));
    printf("%d\n",prime_length("kittens"));
    printf("%d\n",prime_length("orange"));
}
```
This code defines a function `prime_length()` which checks if the length of the provided string is a prime number. It does this by iterating from 2 to the square root of the length of the string and checking if the string length is divisible by any of these numbers. If it is, it returns `false`, otherwise it returns `true`.

The `main()` function tests the `prime_length()` function with various strings.

Note: This code is written in C++.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_prime(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int prime_length(char* str) {
    return is_prime(strlen(str));
}

int main() {
    printf("%d\n", prime_length("Hello"));
    printf("%d\n", prime_length("abcdcba"));
    printf("%d\n", prime_length("kittens"));
    printf("%d\n", prime_length("orange"));
    return 0;
}
```
This code defines a function `prime_length()` which checks if the length of the provided string is a prime number. It does this by calling `is_prime()` function which checks if the given number is a prime number. It then uses the `strlen()`