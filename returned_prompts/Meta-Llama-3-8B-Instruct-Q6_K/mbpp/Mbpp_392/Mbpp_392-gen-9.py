```
def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 2:
            return k
        max_sum = k
        for i in range(2, 6):
            if i * (i + 1) // 2 > k:
                break
            if i > 1 and k % i == 0:
                max_sum = max(max_sum, f(k // i) + k)
        memo[k] = max_sum
        return max_sum
    return f(n)
```
The problem is to find the maximum sum of numbers that can be obtained using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). The function f(n) represents the maximum sum that can be obtained from the numbers from 1 to n.

The given unit test `assert get_max_sum(60) == 106` suggests that the maximum sum for the number 60 is 106.

To solve this problem, we can use dynamic programming to store the maximum sum for each number in a dictionary. The function f(n) is defined recursively as follows: if k is in the dictionary, return the stored value; otherwise, calculate the maximum sum by iterating over the possible divisors of k and recursively calling f(n/2), f(n/3), f(n/4), and f(n/5), and update the dictionary with the calculated value.

The time complexity of this solution is O(n log n) and the space complexity is O(n), where n is the input number. This is because we need to store the maximum sum for each number from 1 to n in the dictionary, and the time complexity is dominated by the recursive calls and the dictionary lookups.

Here is the Python code that implements the above solution:
```
def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 2:
            return k
        max_sum = k
        for i in range(2, 6):
            if i * (i + 1) // 2 > k:
                break
            if i > 1 and k % i == 0:
                max_sum = max(max_sum, f(k // i) + k)
       