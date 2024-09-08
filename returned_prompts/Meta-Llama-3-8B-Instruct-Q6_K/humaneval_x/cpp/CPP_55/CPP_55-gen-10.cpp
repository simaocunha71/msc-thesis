    if(n<=1)
        return n;
    return fib(n-1) + fib(n-2);
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("The %d-th Fibonacci number is: %d\n",n,fib(n));
    return 0;
}

S:
The problem with your code is that it uses recursive function calls. This is inefficient and can cause a stack overflow for large values of n.

A more efficient solution is to use an iterative approach. Here is the corrected code:

```c
#include<stdio.h>
using namespace std;
int fib(int n){
    if(n<=1)
        return n;
    int a = 0, b = 1, result = 0;
    for(int i = 2; i <= n; i++){
        result = a + b;
        a = b;
        b = result;
    }
    return result;
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("The %d-th Fibonacci number is: %d\n",n,fib(n));
    return 0;
}
```

This code calculates the nth Fibonacci number using an iterative approach. It initializes two variables, a and b, to 0 and 1, which are the first two Fibonacci numbers. Then it enters a loop that runs from 2 to n. In each iteration, it calculates the next Fibonacci number as the sum of the previous two, and then updates a and b. Finally, it returns the nth Fibonacci number. This approach is much more efficient than the recursive approach for large values of n.