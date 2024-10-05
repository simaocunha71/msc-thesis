```go
func GetOddCollatz(n int) []int {
    collatz := []int{n}
    for n != 1 {
        if n%2 == 0 {
            n /= 2
        } else {
            n = 3*n + 1
        }
        collatz = append(collatz, n)
    }
    sort.Slice(collatz, func(i, j int) bool {
        return collatz[i]%2 != 0 && collatz[j]%2 != 0 && collatz[i] < collatz[j]
    })
    var result []int
    for _, v := range collatz {
        if v%2 != 0 {
            result = append(result, v)
        }
    }
    return result
}
```

This solution works by generating the Collatz sequence for the given number `n`. It then sorts the sequence in increasing order, filtering out the odd numbers. Finally, it returns the sorted list of odd numbers.