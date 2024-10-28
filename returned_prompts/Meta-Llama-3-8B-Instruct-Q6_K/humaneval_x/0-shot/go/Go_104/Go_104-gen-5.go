Here is a Go program that solves the problem:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        numStr := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range numStr {
            digit, _ := strconv.Atoi(string(c))
            if digit%2 == 0 {
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

In this program, we iterate over each number in the input slice. For each number, we convert it to a string and iterate over each character (digit) in the string. If we find a digit that is even (i.e., its remainder when divided by 2 is 0), we set a flag `hasEvenDigit` to `true`. If `hasEvenDigit` is still `false` after checking all digits, we append the number to the result slice. Finally, we sort the result slice and return it.

For example, if we call `UniqueDigits([]int{15, 33, 1422, 1})`, the output will be `[1, 15, 33]`. If we call `UniqueDigits([]int{152, 323, 1422, 10})`, the output will be `[]`.