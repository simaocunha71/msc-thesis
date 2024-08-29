/*
Return true if a given number is prime, and false otherwise.
>>> is_prime(6)
false
>>> is_prime(101)
true
>>> is_prime(11)
true
>>> is_prime(13441)
true
>>> is_prime(61)
true
>>> is_prime(4)
false
>>> is_prime(1)
false
*/
#include<stdio.h>
using namespace std;
bool is_prime(long long n){
    if (n == 2)
        return true;
    if (n < 2 || n % 2 == 0)
        return false;
    for (long long i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;
    return true;
}
请问以上代码是否有错误，如果有错误请指出错误所在

这个代码是正确的。它实现了检查一个数是否为质数的功能。函数 `is_prime` 接受一个 `long long` 类型的参数 `n`，并返回一个布尔值，表示 `n` 是否为质数。

以下是对代码的解释：

- 如果 `n` 等于 2，则返回 `true`，因为 2 是最小的质数。
- 如果 `n` 小于 2 或者 `n` 是偶数（`n % 2 == 0`），则返回 `false`，因为小于 2 的数和偶数都不是质数。
- 对于其他情况，从 3 开始，每次增加 2（因为偶数不可能是质数），检查 `n` 是否能被当前的数整除。如果能被整除，则返回 `false`，因为 `n` 不是质数。
- 如果 `n` 不能被任何小于等于其平方根的数整除，则返回 `true`，因为 `n` 是质数。

这个算法的复杂度是 O(sqrt(n))，因为只需要检查到 `n` 的平方根。这是检查一个数是否为质数的最有效算法之一。
