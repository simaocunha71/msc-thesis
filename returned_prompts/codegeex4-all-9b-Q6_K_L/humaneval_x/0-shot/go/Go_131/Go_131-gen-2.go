```go
func Digits(n int) int {
    product := 1
    isOdd := false
    for n > 0 {
        digit := n % 10
        if digit%2 == 1 {
            product *= digit
            isOdd = true
        }
        n /= 10
    }
    if !isOdd {
        return 0
    }
    return product
}
```

This solution is correct and efficient. It iterates through each digit of the input number, checks if it's odd, and if so, multiplies it to the product. It also keeps track of whether any odd digit has been found. If no odd digit is found, it returns 0. Otherwise, it returns the product of the odd digits.
