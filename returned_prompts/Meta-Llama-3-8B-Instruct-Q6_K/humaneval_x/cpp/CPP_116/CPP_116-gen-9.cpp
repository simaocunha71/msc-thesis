The problem is asking to sort a vector of integers based on two conditions. First, the number of ones in the binary representation of the integer in ascending order. If two integers have the same number of ones, then they should be sorted based on their decimal value in ascending order.

The problem can be solved by using the sort function from the algorithm library in C++. We can use a lambda function as a comparison function for the sort function.

Here is the solution:
```cpp
#include <vector>
#include <algorithm>

std::vector<int> sort_array(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), [](int a, int b) {
        int count_a = __builtin_popcount(a);
        int count_b = __builtin_popcount(b);
        if (count_a == count_b) {
            return a < b;
        }
        return count_a < count_b;
    });
    return arr;
}
```
In this solution, the `sort_array` function takes a vector of integers as input and returns a sorted vector. The `sort` function is used to sort the vector, and a lambda function is used as the comparison function.

The lambda function compares two integers `a` and `b` by first counting the number of ones in their binary representation using the `__builtin_popcount` function. If the number of ones is the same for both integers, then the function returns `true` if `a` is less than `b`, and `false` otherwise. If the number of ones is different, then the function returns `true` if the number of ones in `a` is less than the number of ones in `b`.

The `sort` function uses this comparison function to sort the vector. The sorted vector is then returned by the `sort_array` function.

You can test this function with a sample