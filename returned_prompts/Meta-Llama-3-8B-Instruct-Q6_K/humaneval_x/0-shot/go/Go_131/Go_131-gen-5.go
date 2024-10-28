```go
func Digits(n int) int {
    product := 1
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= int(digit)
        }
        n /= 10
    }
    return product
}
```


Explanation:
The problem is asking to calculate the product of all the odd digits in a given positive integer. We can solve this by iterating over each digit of the number, checking if it's odd, and if so, multiplying the product by that digit.

In the code, we initialize a product variable to 1. Then, we loop until the number becomes 0. Inside the loop, we extract the last digit of the number using the modulus operator (`n % 10`). If the digit is odd (i.e., `digit % 2 != 0`), we multiply the product by that digit. Finally, we remove the last digit from the number by integer division (`n /= 10`).

The function returns the calculated product. If all digits are even, the product will be 0, as required.