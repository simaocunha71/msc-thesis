        int product = 1;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
            }
            n /= 10;
        }
        return product;
    }
} 







C++:
```cpp
#include <bits/stdc++.h>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}
```

Python:
```python
def digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10
    return product
```







Python:
```python
def digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10
    return product
```

Explanation:
The solution iterates through each digit of the input integer `n` from right to left using the modulus operator (`%`) to extract the last digit. It checks if the digit is odd by using the modulus operator (`%`) with 2, and if it is, it multiplies the product by the digit. The process is repeated until all digits have been processed. The final product is returned. If all digits are even, the product will be 0, which is the desired result.