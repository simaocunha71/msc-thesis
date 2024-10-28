Here's a solution in C++:

```cpp
#include <iostream>

int digits(int n) {
    if (n == 0) {
        return 0;
    }
    int a = n % 10;
    if (a % 2 == 1) {
        return a * digits(n / 10);
    } else {
        return digits(n / 10);
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << digits(n) << std::endl;
    return 0;
}
```

This solution defines a function `digits` that takes an integer `n` as input. It first checks if `n` is equal to 0, and if so, it returns 0. Otherwise, it extracts the last digit of `n` by taking the remainder of `n` divided by 10 and stores it in the variable `a`. If `a` is an odd number (i.e., `a % 2 == 1`), it multiplies `a` by the result of `digits(n / 10)` and returns the product. Otherwise, it simply calls `digits(n / 10)` to recursively process the remaining digits of `n`.

In the `main` function, the program reads an integer `n` from the user and calls the `digits` function with `n` as the input. Finally, it prints the result using `std::cout`.

This solution correctly calculates the product of the odd digits in the given number and returns 0 if all digits are even.

Note: Make sure to include the necessary libraries (`<iostream>` and `