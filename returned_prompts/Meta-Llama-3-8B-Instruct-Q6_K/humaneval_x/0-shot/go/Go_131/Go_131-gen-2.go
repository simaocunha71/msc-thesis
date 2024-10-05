```
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


Explanation:
The function takes an integer `n` as input and returns the product of its odd digits. If all digits are even, the function returns 0.

Here's how the function works:
1. Initialize a variable `product` to 1. This will store the product of the odd digits.
2. Loop through the digits of `n` from right to left using a for loop.
3. In each iteration, extract the last digit of `n` using the modulus operator (`%`).
4. Check if the digit is odd by using the modulus operator again (`% 2 != 0`). If the digit is odd, multiply `product` by the digit.
5. Divide `n` by 10 to move to the next digit.
6. Repeat steps 3-5 until `n` becomes 0.
7. Return the final value of `product`.

For example, if `n` is 235, the function will calculate the product of the odd digits (3 and 5) and return 15. If `n` is 4, the function will return 0 because all digits are even.