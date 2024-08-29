```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> count_up_to(int n) {
    vector<int> primes;
    if (n <= 2) return primes; // No primes less than 2
    primes.push_back(2); // Add the first prime number
    for (int i = 3; i < n; i += 2) { // Start from 3 and step by 2 to skip even numbers
        bool is_prime = true;
        for (int j = 2; j <= sqrt(i); j++) { // Check divisibility up to the square root of i
            if (i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) primes.push_back(i);
    }
    return primes;
}

int main() {
    int n = 20;
    vector<int> result = count_up_to(n);
    for (int prime : result) {
        cout << prime << " ";
    }
    cout << endl;
    return 0;
}
```