        if  (n  == 0)  return 0;
        if  (n  == 1)  return 0;
        if  (n  == 2)  return 2;
        if  (n  == 3)  return 0;

        int[] fibs 
            = new int[] {0, 0, 2, 0};

        for  (int i = 4; i <= n; i++)  {
            int next = fibs[3] + fibs[2] + fibs[1] + fibs[0];
            fibs[0] = fibs[1];
            fibs[1] = fibs[2];
            fibs[2] = fibs[3];
            fibs[3] = next;
        }
        return fibs[3];
    }
}


A: Here's the answer to your question:

The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows: fib4(0) -> 0, fib4(1) -> 0, fib4(2) -> 2, fib4(3) -> 0, fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4). Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.

Here is the Python code to solve this problem:

```python
def fib4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fibs = [0, 0, 2, 0]

    for i in range(4, n+1):
        next = fibs[3] + fibs[2] + fibs[1] + fibs[0]
        fibs[0] = fibs[1]
        fibs[1] = fibs[2]
        fibs[2] = fibs[