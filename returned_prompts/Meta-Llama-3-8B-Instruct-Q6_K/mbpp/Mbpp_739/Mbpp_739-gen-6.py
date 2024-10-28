```
def find_Index(n):
    def triangular_number(k):
        return k*(k+1)//2

    i = 1
    while True:
        if len(str(triangular_number(i))) == n:
            return i
        i += 1
``` 

This function uses a helper function `triangular_number` to calculate the `i`th triangular number. It then iterates over `i` until it finds the smallest triangular number with `n` digits, and returns the index `i`. The unit test `assert find_Index(2) == 4` ensures that the function works correctly. 

Please note that Python's integer division (//) is used to calculate the triangular number. This is because we are dealing with large numbers and we don't want to lose any digits due to floating point precision. 

The time complexity of this function is O(n), where n is the number of digits. This is because in the worst case, we need to iterate over `i` up to `10**n-1` to find the smallest triangular number with `n` digits. 

The space complexity is O(1), as we are using a constant amount of space to store the variables `i` and `n`. 