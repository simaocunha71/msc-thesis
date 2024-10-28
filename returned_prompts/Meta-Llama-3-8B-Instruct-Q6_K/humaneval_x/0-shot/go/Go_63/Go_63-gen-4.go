The given problem can be solved using dynamic programming. The idea is to store the previously computed values of the Fibfib sequence in an array and use these values to compute the next value.

Here is the Python solution for the given problem:

```python
def Fibfib(n):
    if n <= 1:
        return 0
    fibfib_values = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_values.append(fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3])
    return fibfib_values[n]
```

This function initializes the Fibfib sequence with the base cases (Fibfib(0) == 0, Fibfib(1) == 0, Fibfib(2) == 1). Then, it iterates from 3 to n, computing each Fibfib value as the sum of the previous three values. Finally, it returns the n-th Fibfib value. This approach has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.