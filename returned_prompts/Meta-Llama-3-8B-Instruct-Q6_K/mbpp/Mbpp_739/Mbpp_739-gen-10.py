```
def find_Index(n):
    i = 1
    while True:
        tri = (i * (i + 1)) // 2
        if len(str(tri)) == n:
            return i
        i += 1
```    
The function `find_Index` takes an integer `n` as input and returns the index of the smallest triangular number with `n` digits. It uses a while loop to generate triangular numbers and checks if the length of the string representation of the triangular number is equal to `n`. If it is, the function returns the current index `i`. If not, the function increments `i` and continues the loop. The unit test `assert find_Index(2) == 4` ensures that the function works correctly for `n = 2`. 

The `//` operator is used for integer division, which returns the integer part of the division result. The `len(str(tri))` expression calculates the length of the string representation of the triangular number `tri`. The `str(tri)` expression converts the integer `tri` to a string. The `assert` statement checks if the output of the `find_Index` function for `n = 2` is equal to `4`. If the output is not equal to `4`, the `assert` statement raises an `AssertionError`. 

Note that this function assumes that the input `n` is a positive integer. If `n` is not a positive integer, the function may not work correctly. You may want to add input validation to handle this case. For example, you could add a check at the beginning of the function to raise a `ValueError` if `n` is not a positive integer. 

Here is the modified function with input validation:
```
def find_Index(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    i = 1
    while True:
        tri = (i * (i + 1)) // 2
        if len(str(tri)) == n:
            return i
        i += 1
```   


This function will work correctly for any positive integer input `n`, and it will raise a `ValueError` if `n` is not a positive integer. You can use this function to find the index of the smallest triangular number with `n` digits for any positive integer `n`.  



The time complexity of this function