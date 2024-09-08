    if (n <= 1) {
        return 1;
    }
    int res = 1;
    while (n > 1) {
        if (n % 2 == 1) {
            res = (res * p) % p;
        }
        p = (p * p) % p;
        n /= 2;
    }
    return res;
}

int main() {
    printf("%d\n", modp(3, 5));
    printf("%d\n", modp(1101, 101));
    printf("%d\n", modp(0, 101));
    printf("%d\n", modp(3, 11));
    printf("%d\n", modp(100, 101));
    return 0;
}
C++:
```
#include <iostream>

using namespace std;

int modp(int n, int p) {
    if (n <= 1) {
        return 1;
    }
    int res = 1;
    while (n > 1) {
        if (n % 2 == 1) {
            res = (res * p) % p;
        }
        p = (p * p) % p;
        n /= 2;
    }
    return res;
}

int main() {
    cout << modp(3, 5) << endl;
    cout << modp(1101, 101) << endl;
    cout << modp(0, 101) << endl;
    cout << modp(3, 11) << endl;
    cout << modp(100, 101) << endl;
    return 0;
}
```
Explanation:
The modp function calculates 2^n modulo p. It uses the property of modular arithmetic that (a * b) % p = ((a % p) * (b % p)) % p.

The function first checks if n is less than or equal to 1. If it is, the function returns 1 because 2^0 and 2^1 are both equal to 1 modulo any prime p.

If n is greater than 1, the function initializes a result variable to 1. It then enters a loop that continues until n is less than or equal to 1.

In each iteration of the loop, the function checks if n is odd. If it is, the function multiplies the result by p modulo p. This is done by calculating the result modulo p