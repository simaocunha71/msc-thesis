The problem is asking to write a function to efficiently compute the n-th element of the fibfib number sequence. The fibfib number sequence is defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

The problem can be solved by using dynamic programming to store the intermediate results and avoid the redundant calculations. Here is the Python solution:
```
def fibfib(n: int):
    if n <= 1:
        return 0
    fibfib_values = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_values.append(fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3])
    return fibfib_values[n]
```
The function first checks if the input number is less than or equal to 1, if so, it returns 0. Then it initializes a list `fibfib_values` with the first three elements of the sequence. The function then iterates from 3 to n, and for each iteration, it calculates the next element of the sequence by adding the previous three elements. Finally, it returns the n-th element of the sequence.

This solution has a time complexity of O(n) and a space complexity of O(n), which is efficient for large input values. The function also passes the given unit tests.