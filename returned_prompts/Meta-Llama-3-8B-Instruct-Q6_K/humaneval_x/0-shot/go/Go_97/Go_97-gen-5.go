```go
func Multiply(a, b int) int {
    // Calculate unit digits of a and b
    unitA := a % 10
    unitB := b % 10
    
    // Calculate product of unit digits
    product := unitA * unitB
    
    // If a or b is negative, multiply product by -1
    if (a < 0 && b > 0) || (a > 0 && b < 0) {
        product = -product
    }
    
    return product
}
```


Explanation:
The problem is asking to create a function that takes two integers and returns the product of their unit digits. The unit digit of a number is the last digit of the number. For example, the unit digit of 148 is 8.

In the given code, we calculate the unit digits of `a` and `b` by using the modulus operator `%`. The unit digit of a number is the remainder when the number is divided by 10.

We then calculate the product of the unit digits and check if either `a` or `b` is negative. If either of them is negative, we multiply the product by -1 to get the correct result.

Finally, we return the product as the result of the function.

For example, if we call `Multiply(148, 412)`, the function will calculate the unit digits of 148 and 412, which are 8 and 2 respectively. The product of these unit digits is 16, which is the result of the function. If we call `Multiply(19, 28)`, the function will calculate the unit digits of 19 and 28, which are 9 and 8 respectively. The product of these unit digits is 72, which is the result of the function. If we call `Multiply(2020, 1851)`, the function will calculate the unit digits of 2020 and 1851, which are 0 and 1 respectively. The product of these unit digits is 0, which is the result of the function. If we call `Multiply(14, -15)`, the function will calculate the unit digits of 14 and -15, which are 4 and 5 respectively. The product of these unit digits is 20, which is the result of the function.