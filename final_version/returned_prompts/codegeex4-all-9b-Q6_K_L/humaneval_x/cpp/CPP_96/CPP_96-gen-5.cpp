```cpp
#include <stdio.h>
#include <vector>
using namespace std;

vector<int> count_up_to(int n) {
    vector<int> primes;
    for (int i = 2; i < n; i++) {
        bool is_prime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            primes.push_back(i);
        }
    }
    return primes;
}

int main() {
    vector<int> result = count_up_to(20);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

This code defines a function `count_up_to` that takes an integer `n` and returns a vector of prime numbers less than `n`. The function uses a nested loop to check if each number is prime, and if so, adds it to the vector. The main function demonstrates how to use this function.