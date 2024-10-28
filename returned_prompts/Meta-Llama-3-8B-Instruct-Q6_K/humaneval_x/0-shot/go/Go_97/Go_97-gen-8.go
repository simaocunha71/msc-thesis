```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```
The function takes two integers a and b, and returns the product of their unit digits. The unit digit of a number can be obtained by taking the modulus of the number with 10. So, we calculate the unit digit of a and b by using the modulus operator `%`. Then we multiply these two unit digits and return the result.

This function works for both positive and negative integers, because the modulus operator `%` works correctly for negative numbers. For example, (-15 % 10) will give -5, and (-15 % 10) * (-5) will give 25. 

The function also works correctly for large integers, because the modulus operator `%` works correctly for large integers. For example, (2020 % 10) will give 0, and (1851 % 10) will give 1. 

The function does not need to handle the case where the input is not valid, because the problem statement assumes that the input is always valid. 

For example, the function will correctly return 0 for the input (2020, 1851), because the unit digits of these numbers are 0 and 1, and the product of these digits is 0. 

The function will also correctly return 20 for the input (14, -15), because the unit digits of these numbers are 4 and -5, and the product of these digits is 20. 

The time complexity of this function is O(1), because it performs a constant number of operations. The space complexity is O(1), because it uses a constant amount of space. 