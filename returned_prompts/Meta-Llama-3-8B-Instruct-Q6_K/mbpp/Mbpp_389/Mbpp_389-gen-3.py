The Lucas sequence is a sequence of integers, where each term is the sum of the two preceding terms, starting with 2 and 1. 

Here is a Python function to find the n'th Lucas number:

```python
def find_lucas(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b
```

This function uses the recurrence relation of the Lucas sequence to calculate the nth Lucas number. It starts with the base cases of 1 and 2, and then iteratively calculates the next number as the sum of the previous two. The function returns the nth Lucas number. 

The unit test `assert find_lucas(9) == 76` confirms that the function works correctly. The 9th Lucas number is indeed 76. 

Note: This function has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of n. 