    if(n <= 1) return n;
    int a = 0, b = 1, res = 0;
    for(int i = 2; i <= n; i++){
        res = a + b;
        a = b;
        b = res;
    }
    return res;
}

int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th Fibonacci number is: %d\n", n, fib(n));
    return 0;
}

B:
```
Here is the Python code for the same problem:

```Python
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

n = int(input("Enter the value of n: "))
print("The {}-th Fibonacci number is: {}".format(n, fib(n)))
```

Explanation:
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function `fib(n)` calculates the `n-th` Fibonacci number.

In the Python code, we define a function `fib(n)` that calculates the `n-th` Fibonacci number. We initialize two variables `a` and `b` to 0 and 1 respectively, which are the first two numbers in the Fibonacci sequence. We then use a for loop to calculate the next `n-2` numbers in the sequence. In each iteration of the loop, we update `a` and `b` to be the last two numbers in the sequence. Finally, we return the `n-th` Fibonacci number, which is stored in `b`.

In the `main()` function, we prompt the user to enter the value of `n` and then call the `fib(n)` function to calculate the `n-th` Fibonacci number. We then print the result.

The C++ code is similar, it uses a for loop to calculate the Fibonacci sequence and then returns the `n-th` Fibonacci number. The main function prompts the user to enter the value of `n` and then calls the `fib(n)` function to calculate the `n-th` Fibonacci number and prints the result.```


C:
```C
#include <stdio.h>

int fib(int n) {
    if (