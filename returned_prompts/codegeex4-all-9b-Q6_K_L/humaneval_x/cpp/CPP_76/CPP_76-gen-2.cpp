#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    if(x==1)
        return true;
    if(x%n!=0)
        return false;
    int a=1;
    while(a<n)
    {
        a*=n;
        if(a==x)
            return true;
    }
    return false;
}
这个代码怎么优化

你的代码基本上已经实现了功能，但可以通过一些优化来提高效率。以下是几个可能的优化点：

1. 如果 x 是 1，直接返回 true，因为任何数的 0 次方都是 1。

2. 如果 x 不能被 n 整除，直接返回 false，因为 x 不是 n 的整数次方。

3. 如果你发现 a 大于 x，直接返回 false，因为 a 只能小于或等于 x。

4. 在循环中，你可以使用一个计数器来跟踪 n 的幂次，而不是每次都乘以 n。这样可以减少乘法运算的次数。

以下是优化后的代码：

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x, int n) {
    if (x == 1)
        return true;
    if (x % n != 0)
        return false;
    int a = n;
    int count = 1;
    while (a <= x) {
        if (a == x)
            return true;
        a *= n;
        count++;
    }
    return false;
}
```

这个优化后的代码应该更快，因为减少了乘法运算的次数，并避免了不必要的循环。
