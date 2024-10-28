```
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
The function `Digits` takes an integer `n` as input and returns the product of its odd digits. If all digits are even, it returns 0.

Here's how it works:

1. Initialize a variable `product` to 1, which will store the product of the odd digits.
2. Loop until `n` is 0.
3. In each iteration, extract the last digit of `n` using the modulo operator (`n % 10`).
4. Check if the digit is odd by using the modulo operator again (`digit % 2 != 0`). If it is odd, multiply the current `product` by the digit.
5. Divide `n` by 10 to move to the next digit.
6. Return the final `product` value.

For example, if `n` is 235, the function will iterate as follows:

* `n` is 235, `digit` is 5, `product` is 1, `n` is 23
* `n` is 23, `digit` is 3, `product` is 15, `n` is 2
* `n` is 2, `digit` is 2, `product` is 15, `n` is 0

The function returns the final `product` value, which is 15. If `n` were 4, the function would return 0, as all digits are even.