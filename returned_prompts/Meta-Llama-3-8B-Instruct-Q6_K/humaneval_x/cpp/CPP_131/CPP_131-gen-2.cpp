The given problem is asking to find the product of all odd digits of a given integer. For example, if the input is 235, the product of odd digits will be 3*5 = 15.

Here is the C++ code to solve this problem:

```cpp
#include <iostream>
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

int main() {
    cout << digits(235) << endl;
    return 0;
}
```

Explanation:
- We initialize a variable `product` to 1.
- We use a while loop to traverse the digits of the input number `n`.
- Inside the loop, we calculate the last digit of `n` using the modulus operator `%`.
- If the digit is odd (i.e., `digit % 2 != 0`), we multiply `product` with the digit.
- We then remove the last digit from `n` by performing integer division by 10.
- The loop continues until all digits of `n` are processed.
- Finally, we return the product of all odd digits.

In the main function, we call the `digits` function with the input 235 and print the result. The output will be 15, which is the product of the odd digits 3 and 5.