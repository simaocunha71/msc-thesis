```
def find_Index(n):
    i = 1
    while True:
        tri_num = (i * (i + 1)) // 2
        if len(str(tri_num)) == n:
            return i
        i += 1
```  
This function uses the formula for the nth triangular number to generate triangular numbers and checks the length of the string representation of each number. When the length of the string representation equals the desired number of digits, the function returns the index of the smallest triangular number with n digits. The unit test `assert find_Index(2) == 4` ensures that the function works correctly. 

The time complexity of this function is O(n^2) because it generates triangular numbers and checks their length. The space complexity is O(1) because it only uses a constant amount of space to store variables. 

Note that the function will run indefinitely if no triangular number with n digits exists. In practice, the function would typically be used with a known upper bound for n, and the function would be designed to return a value indicating that no such triangular number exists if the loop runs too long.  For example, you could add a timeout or a maximum number of iterations before returning a value.  However, in this simple implementation, the function will run indefinitely if no triangular number with n digits exists. 

The function could be optimized by using a more efficient method to generate triangular numbers or by using a more efficient method to check the length of the string representation of the numbers.  For example, you could use a formula to calculate the length of the string representation of the triangular numbers instead of generating the numbers and checking their length.  However, the current implementation is simple and easy to understand. 

The function could also be optimized by using a more efficient method to find the index of the smallest triangular number with n digits.  For example, you could use a binary search to find the index of the smallest triangular number with n digits.  However, the current implementation is simple and easy to understand. 

The function could also be optimized by using a more efficient method to generate triangular numbers.  For example, you could use a formula to generate the triangular numbers instead of using the formula for the nth triangular number.  However, the current implementation is simple and easy to understand. 

The function could also be optimized by using a more efficient method to check the length of the string representation of the numbers.  For example, you could use a formula to calculate the length of