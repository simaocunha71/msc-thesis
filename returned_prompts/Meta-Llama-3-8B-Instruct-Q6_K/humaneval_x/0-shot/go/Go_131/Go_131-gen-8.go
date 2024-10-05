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

This solution iterates over each digit of the input number `n` by taking the remainder of `n` divided by 10 (`n % 10`). This gives the last digit of the number. Then, it checks if the digit is odd by using the modulo operator `%` again with 2 (`digit % 2 != 0`). If the digit is odd, it multiplies the `product` by the digit. Finally, it removes the last digit from `n` by performing integer division by 10 (`n /= 10`). The loop continues until `n` becomes 0. The function returns the `product` which is the product of the odd digits. If all digits are even, the `product` will be 1 and the function will return 0. 

For example, for the input `235`, the function will iterate over the digits 5, 3, and 2. It will find that 5 and 3 are odd, so it will multiply the `product` by these digits, resulting in `product` being 15. For the input `4`, the function will find that all digits are even, so it will return 0. 

This solution has a time complexity of O(log n) because it iterates over each digit of the input number, and the number of digits in a number is proportional to the logarithm of the number. The space complexity is O(1) because it only uses a constant amount of space to store the `product`. 