def find_Index(n):
    i = 1
    while len(str(i*(i+1)//2)) < n:
        i += 1
    return i


# assert find_Index(2) == 4
# print(find_Index(2))

"""
Write a Python function to find the index of smallest triangular number with n digits.

Explanation
A triangular number is a number that can be represented as a sum of consecutive natural numbers.
For example, 1 + 2 + 3 + 4 + 5 = 15 is a triangular number. Triangular numbers are also called symmetric numbers or equilateral numbers.

Example 1:
Input: 2
Output: 4
Explanation: The smallest triangular number with 2 digits is 10. The index of 10 is 4.

Example 2:
Input: 3
Output: 9
Explanation: The smallest triangular number with 3 digits is 18. The index of 18 is 9.

"""
```
def find_Index(n):
    i = 1
    while len(str(i*(i+1)//2)) < n:
        i += 1
    return i


# assert find_Index(2) == 4
# print(find_Index(2))
```

Explanation:
The function `find_Index` takes an integer `n` as input and returns the index of the smallest triangular number with `n` digits. A triangular number is a number that can be represented as a sum of consecutive natural numbers.

In the function, we initialize a variable `i` to 1. We then enter a while loop that continues until the length of the string representation of `i*(i+1)//2` (which is the formula to calculate a triangular number) is less than `n`. Inside the loop, we increment `i` by 1 until the condition is met. Once the condition is met, we return the value of `i`.

To test the function, we use the `assert` statement to check if the function correctly returns the expected result for the given test case (`find_Index(2) ==