```
def get_max_sum(n):
    """
    :type n: int
    :rtype: int
    """
    def f(n):
        if n in memo: return memo[n]
        if n < 1: return 0
        res = max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)
        memo[n] = res
        return res
    memo = {}
    return f(n)
```

Explanation:
This problem is a classic problem of memoization, which is a technique to store the results of expensive function calls and return the cached result when the same inputs occur again. In this case, we can use a dictionary to store the results of all previous function calls. The function `get_max_sum` returns the maximum sum by using the equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). The function `f` is used to calculate the maximum sum for a given number `n`. The result is stored in the dictionary `memo` for future use.

Here is an example to demonstrate the usage of the function:

```python
print(get_max_sum(60))  # Output: 106
```

In this example, we pass the number 60 to the function `get_max_sum` and it returns the maximum sum for this number.

The time complexity of the function is O(n), where n is the input number. The space complexity is also O(n), as we need to store the results of all previous function calls in the dictionary `memo`.

Overall, this function is a good solution to find the maximum sum possible by using the given equation.

Here are some additional resources for learning more about memoization:

- [Memoization](https://en.wikipedia.org/wiki/Memoization): This Wikipedia page provides a detailed explanation of the memoization technique.
- [Memoization in Python](https://www.geeksforgeeks.org/memoization-in-python/): This GeeksforGeeks article provides a step-by-step guide