```go
func Digits(n int) int {
    var product int
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


Explanation:
The function `Digits(n)` takes an integer `n` as input and returns the product of the odd digits. It iterates through each digit of the number from right to left using the modulus operator (`%`). If the current digit is odd (i.e., `digit % 2 != 0`), it multiplies the product by the current digit. If all digits are even, the function returns 0. The time complexity of this function is O(log10(n)), where `n` is the input integer. This is because the number of digits in an integer is proportional to the logarithm of the integer base 10. The space complexity is O(1), as it only uses a constant amount of space to store the product.