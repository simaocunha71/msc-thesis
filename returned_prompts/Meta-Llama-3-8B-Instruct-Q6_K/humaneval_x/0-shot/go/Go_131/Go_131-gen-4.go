```go
func Digits(n int) int {
    product := 1
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 { // check if the digit is odd
            product *= digit
        }
        n /= 10
    }
    return product
}
```
In this solution, we iterate over each digit of the number by taking the remainder of the number when divided by 10 (`n % 10`), which gives us the last digit. We then divide the number by 10 (`n /= 10`) to move to the next digit. We multiply the product by the current digit if it's odd (`digit % 2 != 0`). If all digits are even, the product will be 1. Finally, we return the product.