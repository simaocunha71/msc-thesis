Here is the C++ code for the problem:
```cpp
#include <cmath>
#include <iostream>

bool isCube(int a) {
    for (int i = 1; i <= std::sqrt(std::abs(a)); i++) {
        if (std::pow(i, 3) == a) {
            return true;
        }
    }
    return false;
}

int main() {
    std::cout << isCube(64) << std::endl;
    return 0;
}
```
Explanation:

The function `isCube` takes an integer `a` as input and returns `true` if `a` is a cube of some integer number, and `false` otherwise.

In the code, we use a loop to iterate from 1 to the square root of the absolute value of `a`. For each iteration, we calculate the cube of the current integer `i` using the `std::pow` function and check if it equals `a`. If it does, we return `true`.

If the loop completes without finding a match, we return `false`.

In the `main` function, we call `isCube` with the input `64` and print the result to the console. The output should be `true`, indicating that `64` is a cube of `4`.