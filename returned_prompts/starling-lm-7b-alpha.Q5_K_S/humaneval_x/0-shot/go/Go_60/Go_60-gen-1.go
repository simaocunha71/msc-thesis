To solve this problem you can use the following steps:

1. Initialize a variable to store the result of the sum. Let's call it "result".
2. Use a "for" loop to iterate from 1 to n (inclusive). Inside the loop, add the current number to the result.
3. After the loop finishes, return the result.

Here's the Python code that implements these steps:

```python
def SumToN(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result
```

You can now use this function to calculate the sum of numbers from 1 to any positive integer.

For example, if you call `SumToN(30)`, it will return 465, as the sum of numbers from 1 to 30. Similarly, `SumToN(100)` will return 5050, `SumToN(5)` will return 15, and `SumToN(10)` will return 55.

The time complexity of this solution is O(n) because we need to iterate through all the numbers from 1 to n. The space complexity is O(1) because we only use a constant amount of extra space to store the result.

To verify the correctness of the solution, you can use mathematical induction. The sum of the first k positive integers is given by the formula:

Sum = k * (k + 1) / 2

For n = 30, the sum is 30 * (30 + 1) / 2 = 465. For n = 100, the sum is 100 * (100 + 1) / 2 = 5050. For n = 5, the sum is 5 * (5 + 1) / 2 = 15. And for n = 10, the sum is 10 * (10 + 1) / 2 = 55.

By following these steps and using the provided Python code, you can solve the problem and calculate the sum of numbers from 1 to any positive integer efficiently.

The provided Python code is an efficient solution