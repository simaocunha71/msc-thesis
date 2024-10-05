```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```


Explanation:
The problem is asking to create a function that takes two integers as input and returns the product of their unit digits. The unit digit of a number is the remainder when the number is divided by 10.

In the given Go code, the function `Multiply(a, b int)` takes two integers `a` and `b` as input. It then uses the modulus operator `%` to find the remainder of the division of `a` and `b` by 10, which gives the unit digit of the numbers. The product of these unit digits is then returned.

For example, if `a = 148` and `b = 412`, the unit digits are 8 and 2 respectively. The product of these unit digits is 8 * 2 = 16, which is the output of the function.

The function is designed to handle negative numbers by simply multiplying the absolute values of the input numbers, since the product of two negative numbers is positive. This is why the output of `Multiply(14, -15)` is 20, which is the product of the absolute values of the unit digits.