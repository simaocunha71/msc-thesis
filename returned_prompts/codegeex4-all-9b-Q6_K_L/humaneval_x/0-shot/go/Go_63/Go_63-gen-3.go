The FibFib number sequence is a sequence similar to the Fibbonacci sequence, but with a different definition. The first two elements are 0, the third is 1, and every subsequent element is the sum of the three preceding ones. 

To compute the nth element of the FibFib sequence, we can use dynamic programming. We will create an array to store the computed values, starting with the base cases FibFib(0) and FibFib(1), which are both 0, and FibFib(2) which is 1. Then, we can iterate from 3 to n, calculating each FibFib(i) as the sum of FibFib(i-1), FibFib(i-2), and FibFib(i-3).

Here is the Python code to compute the nth element of the FibFib sequence:

```python
def Fibfib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib = [0] * (n+1)
        fibfib[2] = 1
        for i in range(3, n+1):
            fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
        return fibfib[n]
```

This function takes an integer n as input and returns the nth element of the FibFib sequence. The time complexity of this function is O(n), and the space complexity is also O(n) because we are using an array to store the computed values.