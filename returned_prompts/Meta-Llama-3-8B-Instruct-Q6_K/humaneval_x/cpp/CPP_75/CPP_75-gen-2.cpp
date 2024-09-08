The function is_multiply_prime checks whether a given number is the product of three prime numbers or not.

Here is a simple and efficient solution in C++:
```cpp
#include <iostream>
using namespace std;

bool is_multiply_prime(int a) {
    for (int i = 2; i <= 100; i++) {
        for (int j = 2; j <= 100; j++) {
            for (int k = 2; k <= 100; k++) {
                if (i * j * k == a) {
                    if (is_prime(i) && is_prime(j) && is_prime(k))
                        return true;
                }
            }
        }
    }
    return false;
}

bool is_prime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    cout << is_multiply_prime(30) << endl;
    return 0;
}
```

This code works by iterating over all possible combinations of three numbers from 2 to 100. For each combination, it checks whether the product of the three numbers equals the given number. If the product equals the given number, it then checks whether each number in the combination is prime using the is_prime function. If all three numbers are prime, the function returns true. If no combination is found where all three numbers are prime, the function returns false. The is_prime function checks whether a number is prime by iterating over all numbers from 2 to the square root of the number and checking whether the number is divisible by any of these numbers. If the number is divisible, it is not prime and the function returns false. If the number is not divisible by any of these numbers, it is prime and the function returns true.