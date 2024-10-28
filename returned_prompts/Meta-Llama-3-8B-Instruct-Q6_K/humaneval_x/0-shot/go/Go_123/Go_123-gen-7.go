Here is the solution to the problem:

```go
func GetOddCollatz(n int) []int {
    var result []int
    for n != 1 {
        if n % 2 == 1 {
            result = append(result, n)
        }
        if n % 2 == 0 {
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

This function works by iterating through the Collatz sequence until it reaches 1. It keeps track of the odd numbers it encounters and appends them to the result slice. Once it reaches 1, it appends 1 to the result slice and returns it. The result slice is then sorted in increasing order using the sort.Ints function from the sort package. The sorted result slice is then returned.