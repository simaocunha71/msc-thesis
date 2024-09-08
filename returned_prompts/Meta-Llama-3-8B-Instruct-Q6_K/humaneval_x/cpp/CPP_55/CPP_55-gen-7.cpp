    if(n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}

int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci number is %d\n", n, fib(n));
    return 0;
}

S:
The problem with the above code is that it is recursive and has exponential time complexity. It will cause a stack overflow for large values of n.

Here is a more efficient solution using dynamic programming:

```cpp
#include <iostream>
using namespace std;

int fib(int n) {
    if(n <= 1)
        return n;

    int fib[n+1]; // Create an array to store Fibonacci numbers
    fib[0] = 0;
    fib[1] = 1;

    for(int i = 2; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    return fib[n];
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci number is %d\n", n, fib(n));
    return 0;
}
```

In this code, we create an array `fib` of size `n+1` to store the Fibonacci numbers. We initialize the first two elements as 0 and 1. Then we use a loop to calculate the rest of the Fibonacci numbers. The time complexity of this solution is O(n). It is efficient for large values of n.