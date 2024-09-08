    double y = pow(n, round(log(x) / log(n)));
    return y == x;
}
int main() {
    printf("%d\n",is_simple_power(1, 4)); // true
    printf("%d\n",is_simple_power(2, 2)); // true
    printf("%d\n",is_simple_power(8, 2)); // true
    printf("%d\n",is_simple_power(3, 2)); // false
    printf("%d\n",is_simple_power(3, 1)); // false
    printf("%d\n",is_simple_power(5, 3)); // false
    return 0;
}

Solution:
The problem can be solved by calculating the power of the base and comparing it with the number. If the power matches the number, then the number is a simple power of the base.

Here is the code in C++:

```cpp
#include <cmath>

bool is_simple_power(int x, int n) {
    double y = pow(n, round(log(x) / log(n)));
    return y == x;
}
```

In this code, we use the `pow` function from the `cmath` library to calculate the power of the base `n`. We use the `round` function to round the result of the logarithm to the nearest integer, and then use the `log` function to calculate the logarithm of `x` with base `n`. If the result of the power calculation matches `x`, then `x` is a simple power of `n`. Otherwise, it's not.

The `main` function is used to test the `is_simple_power` function with different inputs. The output of the program is:

```
1
1
1
0
0
0
```

Which matches the expected results.