Here is a simple C++ program that fulfills your requirements:

```cpp
#include <iostream>
using namespace std;

int x_or_y(int n, int x, int y) {
    if (n < 2)
        return y;
    else if (n == 2)
        return x;
    else {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return y;
        }
        return x;
    }
}

int main() {
    cout << x_or_y(7, 34, 12) << endl;
    cout << x_or_y(15, 8, 5) << endl;
    return 0;
}
```

This program checks whether the number `n` is a prime number or not. If `n` is a prime number, it returns `x`, otherwise, it returns `y`. The `main` function tests this function with the given examples. The output of this program will be:

```
34
5
```

This program works as follows:

- It first checks if `n` is less than 2. If it is, it returns `y` because numbers less than 2 are not prime.
- If `n` is 2, it returns `x` because 2 is a prime number.
- If `n` is greater than 2, it checks if `n` is divisible by any number from 2 to the square root of `n`. If it is, it returns `y` because `n` is not a prime number.
- If `n` is not divisible by any number from 2 to the square root of `n`, it returns `x` because `n` is a prime number.

This program is efficient because it only checks divisibility up to the square root of `n`, which is a well-known optimization for checking primality. It also handles the special