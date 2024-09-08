/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    if(a == 0) {
        return b;
    }
    while(b != 0) {
        if(a > b) {
            a -= b;
        } else {
            b -= a;
        }
    }
    return a;
}
如何优化这个代码

优化这段代码的一个方法是使用欧几里得算法（Euclidean algorithm），这是一种更高效的方法来计算两个数的最大公约数（GCD）。这种方法基于这样一个事实：两个正整数a和b的最大公约数等于b和a除以b的余数的最大公约数。因此，我们可以反复用b替换a，用a除以b的余数替换b，直到b变为0，这时a就是原始两个数的最大公约数。

以下是使用欧几里得算法优化后的代码：

```cpp
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    while(b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
```

这段代码比原来的代码更高效，因为它只需要进行一次循环，而不是像原来的代码那样可能需要进行多次循环。此外，它也更容易理解和实现。
