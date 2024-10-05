You can create a helper function to check whether a number has any even digit. Then, use this function to filter the input list and sort the resulting list. Here is the complete solution:

```go
import (
    "sort"
    "strconv"
)

func hasEvenDigit(n int) bool {
    for _, digit := range strconv.Itoa(n) {
        if digit%2 == 0 {
            return true
        }
    }
    return false
}

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        if !hasEvenDigit(num) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}
```

In this solution, the `hasEvenDigit` function checks whether a given number `n` has any even digit by converting the number to a string and checking each digit. The `UniqueDigits` function uses this helper function to filter the input list and append the numbers without any even digit to the result list. Finally, it sorts the result list and returns it.