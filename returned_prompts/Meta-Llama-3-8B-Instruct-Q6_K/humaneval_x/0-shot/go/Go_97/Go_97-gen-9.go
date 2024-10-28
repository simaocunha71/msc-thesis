```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```

The problem is asking to create a function that takes two integers and returns the product of their unit digits. The unit digit of a number is the last digit of the number. For example, the unit digit of 148 is 8, and the unit digit of 412 is 2.

The function should work for both positive and negative numbers, and should also work for numbers with more than two digits. For example, the unit digit of 2020 is 0, and the unit digit of -15 is 5.

To solve this problem, we can use the modulo operator (%) to extract the last digit of each number. The modulo operator returns the remainder of the division of the number by 10, which is the last digit of the number.

Here is the solution in Go:
```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```
This function works by taking the last digit of each number using the modulo operator, and then multiplying those digits together. The result is the product of the unit digits of the original numbers. For example, calling `Multiply(148, 412)` would return `16`, because the unit digits of 148 and 412 are 8 and 2, and 8 * 2 = 16. Similarly, calling `Multiply(19, 28)` would return `72`, because the unit digits of 19 and 28 are 9 and 8, and 9 * 8 = 72. And so on.