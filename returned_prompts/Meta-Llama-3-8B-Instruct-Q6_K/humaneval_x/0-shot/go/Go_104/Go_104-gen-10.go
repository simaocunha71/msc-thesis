Here is a solution for the problem. This function will iterate over each number in the input list, check if the number has any even digit, and if not, add it to the result list. The result list is then sorted and returned.

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    result := make([]int, 0)
    for _, num := range x {
        hasEvenDigit := false
        for _, digit := range strconv.Itoa(num) {
            d, _ := strconv.Atoi(string(digit))
            if d%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}
```
This function uses a helper function `strconv.Itoa(num)` to convert the number to a string, then iterates over each character (digit) in the string. It converts each character back to an integer using `strconv.Atoi(string(digit))`, and checks if the digit is even by using the modulus operator `%`. If the digit is even, it sets `hasEvenDigit` to `true` and breaks out of the inner loop. If `hasEvenDigit` is still `false` after the inner loop, it adds the number to the result list. Finally, it sorts the result list using `sort.Ints(result)` and returns it. 

The function is then tested with the given examples to verify the correctness of the solution. 

Note: This solution assumes that the input list only contains positive integers, as specified in the problem statement. If the input list can contain negative integers or non-integer values, additional error handling would be required. 

Also, the solution uses the `strconv.Atoi` function, which can panic if the input is not a valid integer. In a production environment, it's a good practice to handle potential errors and panics. 

In this solution, I used the `strconv.Atoi` function without error handling for simplicity. If you need to handle errors, you can use a `try-catch` block or a `if err != nil` statement to handle the error. 

For example:

```go
d, err := strconv.Atoi(string(digit))
if err != nil {
    // handle the error
}
``` 

This would prevent the program from panicking if the input is not a valid integer. 

It's also