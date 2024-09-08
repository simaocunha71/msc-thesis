    if(n==0)
        return 1;
    else
    {
        if(n%2==0)
            return modp(n/2,p)*(modp(n/2,p))%p;
        else
            return ((n%2)*modp(n-1,p))%p;
    }
}
int main()
{
    printf("%d\n", modp(3,5));
    printf("%d\n", modp(1101,101));
    printf("%d\n", modp(0,101));
    printf("%d\n", modp(3,11));
    printf("%d\n", modp(100,101));
    return 0;
}

Solution:
```c
#include <iostream>
using namespace std;

int modp(int n, int p) {
    if (n == 0) {
        return 1;
    } else {
        if (n % 2 == 0) {
            int temp = modp(n / 2, p);
            return (temp * temp) % p;
        } else {
            int temp = modp(n - 1, p);
            return ((n % 2) * temp) % p;
        }
    }
}

int main() {
    printf("%d\n", modp(3, 5));
    printf("%d\n", modp(1101, 101));
    printf("%d\n", modp(0, 101));
    printf("%d\n", modp(3, 11));
    printf("%d\n", modp(100, 101));
    return 0;
}
```

The `modp` function calculates 2^n modulo p, where n is a non-negative integer and p is a prime number. The function uses the property of modular exponentiation, which states that (a*b) % p = ((a % p) * (b % p)) % p. This property is used to reduce the number of calculations and avoid large intermediate results.

The function works by recursively dividing the exponent n by 2 and calculating the square of the result modulo p. If the exponent n is odd, the function calculates the product of the exponent and the result of the previous recursive call modulo p.

The base case of the recursion is when the exponent n is 0, in which case the function returns 1, since 2^0 = 1.

In the `main` function, the `modp` function is called with different