```cpp
#include <vector>

bool is_prime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

std::vector<int> count_up_to(int n) {
    std::vector<int> result;
    for (int i = 2; i < n; ++i) {
        if (is_prime(i)) {
            result.push_back(i);
        }
    }
    return result;
}
```

This code defines a function `is_prime` that checks if a number is prime. The `count_up_to` function then uses this to build a vector of all primes less than `n`. It starts from 2 (the smallest prime number) and goes up to `n - 1`, adding each prime to the result vector.