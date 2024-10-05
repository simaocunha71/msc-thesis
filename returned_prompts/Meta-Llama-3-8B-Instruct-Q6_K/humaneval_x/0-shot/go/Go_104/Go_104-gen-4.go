Here is the Go code that solves the problem:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        s := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range s {
            if c%2 == 0 {
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

This function works by iterating over each number in the input slice. For each number, it checks if the number contains any even digits by converting the number to a string and iterating over each character in the string. If any character is even, it sets a flag to indicate that the number has an even digit. If the number does not have an even digit, it appends the number to the result slice. Finally, it sorts the result slice in increasing order and returns it.