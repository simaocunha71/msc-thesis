Here is a Python solution for the problem:

```Python
def fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c
```

This function uses a for loop to calculate the nth element of the fibfib sequence. It keeps track of the last three elements in the sequence (a, b, c) and updates them in each iteration of the loop. This approach has a time complexity of O(n), which is more efficient than calculating each element from the beginning. 

Here is a Python solution using memoization:

```Python
def fibfib(n, memo = {}):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        memo[n] = result
        return result
```

This function uses a dictionary called memo to store the results of expensive function calls and reuse them when the same inputs occur again. This approach has a time complexity of O(n) as well, but it uses less memory than the previous approach. 

You can also use dynamic programming to solve this problem. The idea is to create an array and fill it with the fibfib sequence. The time complexity of this approach is O(n) as well.

Here is a Python solution using dynamic programming:

```Python
def fibfib(n):
    if n <= 1:
        return 0
    fibfib_sequence = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
    return fibfib_sequence[n]
```

This function creates an array called fibfib_sequence and fills it with the fibfib sequence. The time complexity of this approach is O(n) as well. 

Note: The above solutions are for the Python language, but the idea can be applied to any programming language. The main idea is to use memoization or dynamic programming to store the