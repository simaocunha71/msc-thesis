```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```
The function takes two integers `a` and `b` as input, and returns the product of their unit digits. The unit digit of a number is the remainder when the number is divided by 10. For example, the unit digit of 148 is 8, and the unit digit of 412 is 2.

In the function, we use the modulo operator `%` to get the unit digit of each number. The expression `(a % 10)` gives the unit digit of `a`, and `(b % 10)` gives the unit digit of `b`. We then multiply these two values together and return the result.

For example, if `a = 148` and `b = 412`, then `a % 10` is 8 and `b % 10` is 2, so the function returns `8 * 2 = 16`. If `a = 19` and `b = 28`, then `a % 10` is 9 and `b % 10` is 8, so the function returns `9 * 8 = 72`. And so on.