Here is the solution in Go:

```go
func GetOddCollatz(n int) []int {
    res := make([]int, 0)
    for n != 1 {
        if n % 2 == 1 {
            res = append(res, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    res = append(res, 1)
    sort.Ints(res)
    return res
}
```

This function starts with the given number `n` and iteratively applies the Collatz sequence until it reaches 1. It keeps track of the odd numbers in the sequence by appending them to a slice `res`. After the sequence reaches 1, it appends 1 to the slice and sorts the slice in ascending order using the `sort.Ints` function from the Go standard library. The sorted slice is then returned as the result.