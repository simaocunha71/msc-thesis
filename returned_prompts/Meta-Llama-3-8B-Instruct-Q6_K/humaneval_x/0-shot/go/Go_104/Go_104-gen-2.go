Here is the solution:
```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        str := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range str {
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
Explanation:

1. We iterate over the input list `x` and for each number, we convert it to a string `str` using `strconv.Itoa`.
2. We then iterate over the characters in the string `str` and check if any of them are even digits (i.e., `c%2 == 0`). If we find an even digit, we set `hasEvenDigit` to `true` and break out of the loop.
3. If `hasEvenDigit` is still `false` after checking all characters, we add the original number `num` to the result list `result`.
4. Finally, we sort the result list using `sort.Ints` and return it.

Note that this solution has a time complexity of O(n*m), where n is the length of the input list and m is the maximum length of a string representation of an integer in the list. This is because we iterate over each character in each string representation of an integer. However, this is the most efficient solution possible, since we need to check each digit of each integer to determine if it has an even digit.