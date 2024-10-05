```go
func Digits(n int) int {
    product := 1
    hasOdd := false
    for n > 0 {
        digit := n % 10
        if digit%2 != 0 {
            product *= digit
            hasOdd = true
        }
        n /= 10
    }
    if !hasOdd {
        return 0
    }
    return product
}
```

This solution iterates through each digit of the input number. If the digit is odd, it is multiplied with the current product. If no odd digit is found, the function returns 0. If an odd digit is found, the function returns the product of all odd digits. This solution is efficient and handles all edge cases correctly.