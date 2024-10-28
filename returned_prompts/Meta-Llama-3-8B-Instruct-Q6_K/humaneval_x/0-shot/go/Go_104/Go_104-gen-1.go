Here is a simple and efficient solution in Go:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        if hasOnlyOddDigits(strconv.Itoa(num)) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}

func hasOnlyOddDigits(s string) bool {
    for _, c := range s {
        if c-'0' % 2 == 0 {
            return false
        }
    }
    return true
}
```

This solution iterates over the input list of integers, checks if each integer has only odd digits using the `hasOnlyOddDigits` function, and if it does, adds it to the result list. The `hasOnlyOddDigits` function iterates over the digits of the input string, and returns `false` as soon as it finds a digit that is even. Finally, the solution sorts the result list in increasing order using the `sort.Ints` function and returns it.

The time complexity of this solution is O(n*m), where n is the length of the input list and m is the maximum number of digits in an integer in the list. The space complexity is O(n), as we need to store the result list.