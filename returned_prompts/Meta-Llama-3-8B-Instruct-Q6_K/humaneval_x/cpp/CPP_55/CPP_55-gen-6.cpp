    if(n <=1){
        return n;
    }
    return fib(n-1) + fib(n-2);
}

int main(){
    int n;
    printf("Enter the value of n:");
    scanf("%d",&n);
    printf("The %d-th Fibonacci number is: %d\n",n,fib(n));
    return 0;
}
```

This code is inefficient because it calculates the same Fibonacci numbers multiple times. For example, to calculate `fib(5)`, it calculates `fib(4)` and `fib(3)`, but to calculate `fib(4)`, it calculates `fib(3)` and `fib(2)` again, which means `fib(3)` is calculated twice. This is known as a time complexity of O(2^n).

A more efficient solution would be to use dynamic programming and store the calculated Fibonacci numbers. Here's an example:

```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    int fib[n + 1];
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}

int main() {
    int n;
    printf("Enter the value of n:");
    scanf("%d", &n);
    printf("The %d-th Fibonacci number is: %d\n", n, fib(n));
    return 0;
}
```

In this code, the function `fib(n)` returns the `n`-th Fibonacci number using dynamic programming. The time complexity of this code is O(n). It creates an array `fib` of size `n + 1` and fills it up with the Fibonacci numbers. The `fib` function returns the `n`-th Fibonacci number from the array.

The space complexity is also O(n) because we need to store the Fibonacci numbers in the array. However, we can reduce the space complexity to O(1) if we only need to calculate the `n`-th Fibonacci number and don't need to store the previous Fibonacci numbers. Here's an example:

```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    int a = 0, b =