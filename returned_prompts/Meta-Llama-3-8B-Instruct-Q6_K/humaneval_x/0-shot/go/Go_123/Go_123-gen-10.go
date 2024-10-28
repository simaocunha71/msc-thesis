Here is the solution to the problem:

```go
import (
    "sort"
)

func GetOddCollatz(n int) []int {
    result := make([]int, 0)
    for n != 1 {
        if n%2 == 1 {
            result = append(result, n)
        }
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    result = append(result, 1)
    sort.Ints(result)
    return result
}
```

This function starts with the given number `n` and generates the Collatz sequence until it reaches 1. It keeps track of the odd numbers in the sequence and returns them in sorted order. The function uses the `append` function to add elements to the result slice, and the `sort.Ints` function to sort the slice in ascending order. The function returns the result slice at the end.