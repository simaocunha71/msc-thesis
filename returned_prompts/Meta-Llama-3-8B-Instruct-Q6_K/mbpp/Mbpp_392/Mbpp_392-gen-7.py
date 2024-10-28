```
def get_max_sum(n):
    memo = {1: 1}
    for i in range(2, n + 1):
        memo[i] = max((memo.get(i // 2, 0) + memo.get(i // 3, 0) + memo.get(i // 4, 0) + memo.get(i // 5, 0)), i)
    return memo[n]
``` 

Explanation:
The problem is asking to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). This is a classic example of a dynamic programming problem, where we need to memoize the function calls to avoid redundant computations.

The function get_max_sum takes an integer n as input and returns the maximum sum possible. It uses a dictionary memo to store the results of subproblems. The function iterates from 2 to n and for each number i, it calculates the maximum sum by considering the maximum sum of its divisors (i/2, i/3, i/4, i/5) and the number itself. The maximum sum is stored in the memo dictionary.

The unit test assert get_max_sum(60) == 106 ensures that the function returns the correct result for the input 60. 

This function has a time complexity of O(n) and a space complexity of O(n), where n is the input number. This is because we need to store the results of subproblems in the memo dictionary and iterate from 2 to n. The space complexity can be reduced to O(1) if we don't store the memo dictionary and instead calculate the maximum sum on the fly, but this would increase the time complexity to O(n^2). 