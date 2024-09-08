    if(n<=1)
        return y;
    for(int i=2;i<=n/2;++i)
    {
        if(n%i==0)
            return y;
    }
    return x;
}

int main()
{
    printf("%d\n",x_or_y(15,8,5));
    return 0;
}

```

Here is the solution for the problem:

```cpp
#include <iostream>

using namespace std;

int x_or_y(int n, int x, int y) {
    if (n <= 1) {
        return y;
    }
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            return y;
        }
    }
    return x;
}

int main() {
    cout << x_or_y(15, 8, 5) << endl;
    return 0;
}
```

Explanation:

*   The function `x_or_y` takes three integer parameters: `n`, `x`, and `y`.
*   It first checks if `n` is less than or equal to 1. If true, it returns `y`.
*   Then, it iterates from 2 to `n/2` and checks if `n` is divisible by any of these numbers. If it finds a divisor, it returns `y`.
*   If `n` is not divisible by any of these numbers, it returns `x`.
*   In the `main` function, we call `x_or_y` with the arguments `15`, `8`, and `5`, and print the returned value. The output will be `5`, because `15` is not a prime number. If we call `x_or_y` with a prime number, like `7`, the output will be the value of `x`. For example, `x_or_y(7, 34, 12)` will return `34`.