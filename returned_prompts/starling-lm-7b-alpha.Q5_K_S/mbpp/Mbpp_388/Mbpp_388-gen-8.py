def highest_Power_of_2(n):
    i = 1
    while i <= n:
        i *= 2
    return i/2

# Testing
assert highest_Power_of_2(10) == 8
print("All tests passed.")

"""
Correct Solution:
"""
def highest_Power_of_2(n):
    i = 1
    while i <= n:
        i *= 2
    return i/2

# Testing
assert highest_Power_of_2(10) == 8
print("All tests passed.")

# Time Complexity: O(1)
# Space Complexity: O(1)
```
    
    
    
  
In this solution, we initialize a variable `i` to 1. We then enter a while loop that continues as long as `i` is less than or equal to `n`. Inside the loop, we double the value of `i` in each iteration. When the loop terminates, `i` will be the highest power of 2 that is less than or equal to `n`. We then return `i/2` as the highest power of 2 that is less than or equal to `n`. 

To test the function, we use the `assert` statement to check if the function returns the correct result for the given test case, where `n` is 10 and the expected output is 8. If the assertion passes, the message "All tests passed." is printed, indicating that the function is working correctly. 

The time complexity of this solution is O(1) because the while loop will always terminate after at most one iteration. The space complexity is also O(1) as we only use a constant amount of memory to store the variable `i`. 

Overall, this solution provides a simple and efficient way to find the highest power of 2 that is less than or equal to a given number `n` in Python.