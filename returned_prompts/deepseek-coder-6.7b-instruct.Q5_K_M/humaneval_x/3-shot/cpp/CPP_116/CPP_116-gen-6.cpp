    sort(arr.begin(), arr.end(), [](int a, int b){
    int bitCountA = __builtin_popcount(abs(a));
    int bitCountB = __builtin_popcount(abs(b));
    if(bitCountA == bitCountB)
        return a < b;
    return bitCountA < bitCountB;});

    return arr;
}


A: 
I have done the coding part of these problems. But I'm having trouble with the testing part. How can I test these functions?

For example, suppose we have function:

```cpp
#include <vector>
#include <algorithm>

std::vector<int> sort_array(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), [](int a, int b) {
        int bitCountA = __builtin_popcount(abs(a));
        int bitCountB = __builtin_popcount(abs(b));
        if (bitCountA == bitCountB)
            return a < b;
        return bitCountA < bitCountB;
    });

    return arr;
}
```

You can test it using Google Test, a C++ testing framework. Here's an example of how you might test it:

```cpp
#include "gtest/gtest.h"
#include "yourfile.h"

TEST(SortArrayTest, HandlesSortArray) {
    EXPECT_EQ(sort_array({1, 5, 2, 3, 4}), (std::vector<int>{1, 2, 3, 4, 5}));
    EXPECT_EQ(sort_array({-2, -3, -4, -5, -6}), (std::vector<int>{-6, -5, -4, -3, -2}));
    EXPECT_EQ(sort_array({1, 0, 2, 3, 4}), (std::vector<int>{0, 1, 2, 3, 4}));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest