Here is the C++ code for the problem:

```cpp
#include <iostream>
using namespace std;

int x_or_y(int n, int x, int y) {
    if (n < 2)
        return y;

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return y;
    }
    return x;
}

int main() {
    int n, x, y;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "Enter the value of x: ";
    cin >> x;
    cout << "Enter the value of y: ";
    cin >> y;
    cout << x_or_y(n, x, y) << endl;
    return 0;
}
```

The function `x_or_y(int n, int x, int y)` takes three parameters: `n`, `x`, and `y`. It checks if `n` is less than 2. If it is, the function returns `y`. If `n` is not less than 2, the function checks if `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, the function returns `y`. If `n` is not divisible by any of these numbers, the function returns `x`.

In the `main()` function, we prompt the user to enter the values of `n`, `x`, and `y`. We then call the `x_or_y()` function with these values and print the result.