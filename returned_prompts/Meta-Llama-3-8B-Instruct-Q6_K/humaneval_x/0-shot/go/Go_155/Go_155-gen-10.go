```go
func EvenOddCount(num int) [2]int {
    var even int = 0
    var odd int = 0
    for num != 0 {
        digit := num % 10
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return [2]int{even, odd}
}
```
Explanation:
The function `EvenOddCount` takes an integer as input and returns a tuple of two integers representing the count of even and odd digits respectively.

We initialize two variables `even` and `odd` to keep track of the count of even and odd digits.

We then use a for loop to iterate through each digit of the input integer. We do this by repeatedly dividing the input integer by 10 (using the `/=` operator) until it becomes 0.

For each digit, we use the modulus operator (`%`) to get the remainder of the digit when divided by 2. If the remainder is 0, it means the digit is even, so we increment the `even` variable. Otherwise, the digit is odd, so we increment the `odd` variable.

Finally, we return a tuple of two integers `[even, odd]` representing the count of even and odd digits respectively.

For example, if the input integer is -12, the function will return `(1, 1)` because there is one even digit (2) and one odd digit (1). If the input integer is 123, the function will return `(1, 2)` because there is one even digit (3) and two odd digits (1 and 2).