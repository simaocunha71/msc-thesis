Here is a solution for this problem in Go:

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

In this solution, we iterate over each number in the input list. For each number, we convert it to a string and iterate over each character (digit) in the string. If we find a digit that is even, we set a flag to true and break the loop. After checking all digits, if the flag is still false, we append the number to the result list. Finally, we sort the result list in increasing order and return it.

Note that this solution assumes that the input list contains only positive integers. If the input list can contain negative integers or non-integer values, you may need to add additional error checking code. Also, this solution uses the `strconv` package to convert integers to strings and vice versa, and the `sort` package to sort the result list. These packages are part of the Go standard library.