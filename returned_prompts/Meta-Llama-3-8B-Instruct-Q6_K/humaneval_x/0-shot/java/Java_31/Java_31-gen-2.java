This solution checks if a given number `n` is prime or not. It returns `true` if `n` is prime and `false` otherwise.

The solution first checks if `n` is less than or equal to 1, in which case it is not prime, so it returns `false`.

Then it loops through all numbers `i` from 2 to the square root of `n`. If `n` is divisible by `i`, it means `n` is not prime, so it returns `false`.

If the loop completes without finding any divisors, `n` is prime, so it returns `true`.

Here is the implementation in Java:
```
public boolean isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
```


C++:
```cpp
#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (isPrime(n)) {
        cout << n << " is a prime number." << endl;
    } else {
        cout << n << " is not a prime number." << endl;
    }
    return 0;
}
```

Python:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "