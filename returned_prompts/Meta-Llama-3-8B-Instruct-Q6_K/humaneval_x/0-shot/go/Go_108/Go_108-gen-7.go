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
        sum := 0
        for num > 0 {
            digit := num % 10
            sum += int(digit)
            num /= 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
}
```

This function iterates over the input array, calculates the sum of digits for each number, and increments the count if the sum is greater than 0. If a number is negative, it converts it to positive before calculating the sum of digits. The function returns the total count of numbers with a sum of digits greater than 0.