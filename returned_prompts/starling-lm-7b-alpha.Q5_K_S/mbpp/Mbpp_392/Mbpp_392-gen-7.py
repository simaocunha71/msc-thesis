```
def get_max_sum(n):
    memo = {}
    def f(n):
        if n not in memo:
            max_sum = n
            if n % 2 == 0:
                max_sum = max(max_sum, f(n/2))
            if n % 3 == 0:
                max_sum = max(max_sum, f(n/3))
            if n % 4 == 0:
                max_sum = max(max_sum, f(n/4))
            if n % 5 == 0:
                max_sum = max(max_sum, f(n/5))

            memo[n] = max_sum
        return memo[n]
    return f(n)
```

This function uses a memoization technique to compute the maximum sum in O(log n) time. The idea is to use a dictionary to store the results of the subproblems that have already been computed. If the result of a subproblem is already in the dictionary, the function simply returns it. Otherwise, it computes the result of the subproblem, stores it in the dictionary, and returns it.

The function f(n) is defined inside the outer function get_max_sum. It is a recursive function that computes the maximum sum for a given number n. The base case of the recursion is when n is not in the memo dictionary. In this case, the function computes the maximum sum by recursively calling itself with the divisors of n and adding the results of these recursive calls to the maximum sum. The maximum sum is stored in the memo dictionary for future use.

The outer function get_max_sum calls the function f(n) to compute the maximum sum for the given number n. The result is stored in the memo dictionary and returned by the outer function.

The time complexity of this solution is O(log n) because the function f(n) is called at most log n times due to the recursive calls, and each call takes constant time. The space complexity of the solution is O(log n) because the memo dictionary can store at most log n results of the subproblems.

To test the solution, you can use the assert statement with the example given in