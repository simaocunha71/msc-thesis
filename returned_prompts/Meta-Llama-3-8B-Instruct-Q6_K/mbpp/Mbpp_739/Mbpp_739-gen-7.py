```
def find_Index(n):
    i = 1
    while True:
        tri = i * (i + 1) // 2
        if len(str(tri)) == n:
            return i
        i += 1
``` 

This function generates triangular numbers using the formula `i * (i + 1) // 2` and checks if the number of digits in the triangular number equals `n`. If it does, the function returns the index `i`. If not, the function continues generating triangular numbers until it finds one with the correct number of digits. The unit test `assert find_Index(2) == 4` ensures that the function works correctly. 

For example, the smallest triangular number with 2 digits is `6` (which is `1 * (1 + 1) // 2`), and the smallest triangular number with 3 digits is `10` (which is `2 * (2 + 1) // 2`). The function returns `4` when given `n = 2` because `6` is the smallest triangular number with 2 digits, and its index is `4`. 

This function assumes that `n` is a positive integer. If `n` is not a positive integer, the function may not work correctly. 

This function has a time complexity of O(1) because it generates triangular numbers in a linear fashion, and it checks the number of digits in a constant time. The space complexity is O(1) because it only uses a constant amount of space to store the index and the triangular number. 