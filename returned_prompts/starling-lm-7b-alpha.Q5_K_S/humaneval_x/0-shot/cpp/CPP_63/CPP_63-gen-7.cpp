
The answer is:
fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

The Fibonacci sequence is a sequence defined as follows:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

The FibFib sequence is similar to the Fibonacci sequence, but it starts with 0, 0, 1 instead of 0, 1. Therefore, the FibFib sequence can be defined as follows:
fibfib(0) = 0
fibfib(1) = 0
fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

In this problem, we need to compute the n-th element of the FibFib sequence. By analyzing the definition of the FibFib sequence, we can see that it is similar to the Fibonacci sequence, but it starts with 0, 0, 1. Therefore, we can use the same method to calculate the FibFib sequence as the Fibonacci sequence, and the time complexity is O(n).

Here is a possible solution:

```cpp
#include<stdio.h>
using namespace std;

int fibfib(int n) {
    if (n == 0 || n == 1) return 0;
    if (n == 2) return 1;
    int a = 0, b = 0,