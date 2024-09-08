    if(n==0)
        return 1;
    else
        return (modp(n/2,p)*modp(n/2,p)*pow(2,n%2,p))%p;

}
int main()
{
    printf("%d\n",modp(3,5));
    printf("%d\n",modp(1101,101));
    printf("%d\n",modp(0,101));
    printf("%d\n",modp(3,11));
    printf("%d\n",modp(100,101));
    return 0;
}

S:
The function `modp` calculates `2^n mod p` using the property of modular exponentiation. 

It uses the recursive formula: `2^n mod p = (2^(n/2) mod p)^2 * 2^(n%2) mod p` if `n` is even, and `2^n mod p = 2 mod p` if `n` is odd. 

The base case is when `n` is 0, in which case `2^0 mod p` is 1.

The function also uses the `pow` function from the `<cmath>` library to calculate `(2^(n%2)) mod p`. 

However, the `pow` function is not suitable for large numbers because it can cause overflow. 

To avoid this, we can use the property of modular exponentiation to calculate `(2^(n%2)) mod p` directly without using `pow`. 

Here is the corrected code:

```cpp
#include <iostream>
using namespace std;

int modp(int n, int p) {
    if (n == 0)
        return 1;
    else if (n % 2 == 0) {
        int temp = modp(n / 2, p);
        return (temp * temp) % p;
    } else {
        return (2 % p * modp(n - 1, p)) % p;
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

This code will correctly calculate `2^n mod p` for any positive integer `n