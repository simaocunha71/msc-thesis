    return 0;
}
请帮我补全这个函数

这是一个需要使用斐波那契数列和质数判断的函数，以下是补全的代码：

```c++
#include<cmath>

int prime_fib(int n) {
    int fib1 = 1, fib2 = 2, fib = 1, count = 0;
    while (count < n) {
        fib = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib;
        if (is_prime(fib)) count++;
    }
    return fib;
}

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}
```
在这段代码中，我们首先定义了两个变量 `fib1` 和 `fib2` 来存储斐波那契数列的前两个数，然后定义 `fib` 来存储当前计算出的斐波那契数。我们使用一个 `while` 循环来计算斐波那契数，直到找到第 `n` 个既是斐波那契数也是质数的数。

`is_prime` 函数用于判断一个数是否为质数，它通过检查从 `2` 到 `sqrt(num)` 的所有数是否能整除 `num` 来实现。

注意：这个函数的时间复杂度较高，可能在大 `n` 时会显得较慢。如果你需要处理更大的 `n`，可能需要使用更高效的算法。
