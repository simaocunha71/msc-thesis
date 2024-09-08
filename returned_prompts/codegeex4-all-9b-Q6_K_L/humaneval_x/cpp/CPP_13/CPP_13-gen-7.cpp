/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    int c = a%b;
    int d = b%c;
    if(c==0){
        return d;
    }
    else if(d==0){
        return c;
    }
    else{
        return greatest_common_divisor(c,d);
    }
}
我写了一个递归方法，但是代码中有很多错误，请帮我改正

你的代码中存在一些问题，以下是一些可能的修正：

1. 在你的递归函数中，你首先计算了 `a` 和 `b` 的余数，然后计算了余数和 `b` 的余数。然而，根据欧几里得算法，你应该先计算 `b` 和 `a` 的余数，然后再计算余数和 `a` 的余数。

2. 在你的递归函数中，你检查了 `c` 和 `d` 是否等于 `0`。然而，根据欧几里得算法，你应该检查 `b` 和 `a` 的余数是否等于 `0`。

3. 在你的递归函数中，你返回了 `d` 或 `c`。然而，根据欧几里得算法，你应该返回 `b` 和 `a` 的余数。

以下是修正后的代码：

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    int c = a % b;
    if(c == 0){
        return b;
    }
    else{
        return greatest_common_divisor(b, c);
    }
}
```

这个函数首先计算 `a` 和 `b` 的余数，然后检查余数是否等于 `0`。如果余数等于 `0`，那么 `b` 就是 `a` 和 `b` 的最大公约数。否则，函数会递归地调用自己，用 `b` 和余数作为参数。