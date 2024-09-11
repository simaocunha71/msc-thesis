"""
def find_Odd_Pair(nums, n):
    odd = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (nums[i]^nums[j]) & 1:
                odd += 1
    return odd

if __name__ == '__main__':
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(nums, n):
    odd = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (nums[i]^nums[j]) & 1:
                odd += 1
    return odd

if __name__ == '__main__':
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
```

In the above code, a function named `find_Odd_Pair` is created. This function takes in two parameters, `nums` and `n`. `nums` is a list of integers and `n` is the length of the list. The function then iterates through the list using two nested loops. For each pair of numbers, it calculates the XOR value and checks if it is odd. If it is, the `odd` counter is incremented. Finally, the function returns the total count of pairs with an odd XOR value.

The code includes an assertion to test the function's correctness. It asserts that when the function is called with the list `[5,4,7,2,1]` and the length of the list as 5, the result should be 6.

Overall, this code provides a solution to count the number of pairs whose XOR value is odd in a given list of integers.

```python
def find_Odd_Pair(nums, n):
    odd = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (nums[i]^nums[j]) & 1:
                odd += 