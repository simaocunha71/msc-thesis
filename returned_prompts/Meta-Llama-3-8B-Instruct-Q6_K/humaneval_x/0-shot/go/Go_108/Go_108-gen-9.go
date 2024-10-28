Here is the solution in Go:
```go
import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sumDigits := 0
        for num > 0 {
            digit := num % 10
            sumDigits += digit
            num /= 10
        }
        if sumDigits > 0 {
            count++
        }
    }
    return count
}
```
Here's an explanation of the code:

1. We initialize a counter `count` to 0.
2. We iterate over the input array `arr`.
3. For each number, we check if it's negative. If it is, we take its absolute value.
4. We calculate the sum of the digits of the number using a loop. We use the modulo operator `%` to get the last digit, and then add it to the sum. We then divide the number by 10 to move to the next digit.
5. If the sum of the digits is greater than 0, we increment the `count`.
6. Finally, we return the `count`.

You can test this function with the examples you provided:
```go
fmt.Println(CountNums([]int{})) // 0
fmt.Println(CountNums([]int{-1, 11, -11})) // 1
fmt.Println(CountNums([]int{1, 1, 2})) // 3
```I hope this helps! Let me know if you have any questions.