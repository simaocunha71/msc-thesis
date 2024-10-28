```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```


Explanation:
The problem asks to write a function that takes two integers and returns the product of their unit digits. We can solve this by using the modulus operator `%` to get the last digit of each number and then multiplying them together.

For example, if we call `Multiply(148, 412)`, the function will return `(8 % 10) * (2 % 10) = 8 * 2 = 16`. Similarly, if we call `Multiply(19, 28)`, the function will return `(9 % 10) * (8 % 10) = 9 * 8 = 72`.

The function `Multiply(a, b int) int` takes two integers `a` and `b` as input and returns their product as an integer. The function uses the modulus operator `%` to get the last digit of each number and then multiplies them together. This ensures that the function returns the product of the unit digits of the input integers.