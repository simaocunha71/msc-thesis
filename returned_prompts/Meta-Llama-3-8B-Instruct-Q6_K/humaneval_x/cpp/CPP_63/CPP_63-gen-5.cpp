    if(n <= 2) return 0;
    int a = 0, b = 0, c = 1;
    for(int i = 3; i <= n; i++){
        int temp = a + b + c;
        a = b;
        b = c;
        c = temp;
    }
    return c;
}

int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib sequence is: %d\n", n, fibfib(n));
    return 0;
}

B:
```python
def fibfib(n):
    if n <= 2:
        return 0
    a, b, c = 0, 0, 1
    for i in range(3, n+1):
        a, b, c = b, c, a + b + c
    return c
```

Explanation:
The problem is about the FibFib number sequence, which is similar to the Fibonacci sequence but with an additional term. The sequence is defined as:

fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

To compute the n-th element of this sequence, we can use a dynamic programming approach. The idea is to store the results of previously computed terms and reuse them to compute the next term.

In the C++ solution, we use three variables `a`, `b`, and `c` to store the last three terms of the sequence. We initialize `a` and `b` to 0, and `c` to 1. Then, we loop from 3 to `n`, and in each iteration, we compute the next term as the sum of the last three terms, and update `a`, `b`, and `c` accordingly. Finally, we return the `c` variable, which stores the `n-th` element of the sequence.

In the Python solution, we use a similar approach, but with a slightly different syntax. We use the `range` function to generate a sequence of numbers from 3 to `n+1`, and then we loop over this sequence using a `for` loop. Inside the loop, we update the `a`, `b`, and `