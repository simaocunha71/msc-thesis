```go
func Digits(n int) int {
    product := 1
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    return product
}
```

The solution iterates through each digit of the input number `n` from right to left. For each digit, it checks if the digit is odd by using the modulus operator `%`. If the digit is odd, it multiplies the product by the digit. Finally, it returns the product.

The time complexity is O(log10(n)) where n is the input number. This is because the number of digits in a number is proportional to the logarithm of the number base 10. The space complexity is O(1), as it only uses a constant amount of space to store the product and the current digit.