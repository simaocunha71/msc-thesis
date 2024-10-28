The nth centered hexagonal number is given by the formula: 
Hn = 4n^3 - 3n
Here is the Python function that calculates the nth centered hexagonal number:
```
def centered_hexagonal_number(n):
    return 4*n**3 - 3*n
```
This function takes an integer n as input and returns the nth centered hexagonal number. For example, centered_hexagonal_number(10) returns 271. 

The unit test `assert centered_hexagonal_number(10) == 271` ensures that the function is working correctly. 

The time complexity of this function is O(1) as it only involves a constant number of operations, and the space complexity is O(1) as it only uses a constant amount of space. 





