Here's a function that performs the required task:

```cpp
#include <iostream>
#include <vector>
#include <cmath>

int sum_squares(std::vector<float> lst) {
    int res = 0;
    for (int i = 0; i < lst.size(); i++) {
        int temp = std::ceil(lst[i]);
        res += temp * temp;
    }
    return res;
}

int main() {
    std::vector<float> lst = {-2.4, 1, 1};
    std::cout << sum_squares(lst) << std::endl;
    return 0;
}
```

This function `sum_squares` takes a vector of floats as input and returns an integer. It first initializes a variable `res` to 0, which will store the sum of the squared numbers. Then, it loops through each element in the input vector using a `for` loop.

Inside the loop, it rounds each element in the vector up to the nearest integer using the `ceil` function from the `cmath` library. The rounded element is stored in a temporary variable `temp`. The square of `temp` is added to the `res` variable using the `+=` operator.

After the loop, the function returns the final value of `res`, which is the sum of the squared numbers in the input vector.

In the `main` function, a vector `lst` is created with the values `{-2.4, 1, 1}`. The `sum_squares` function is called with this vector as the argument, and the result is printed to the console using `std::cout`.

The output of this program