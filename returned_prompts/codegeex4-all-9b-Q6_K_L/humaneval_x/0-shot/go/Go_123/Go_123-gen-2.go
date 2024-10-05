```go
func GetOddCollatz(n int) []int {
    collatz := []int{n}
    for n != 1 {
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
        collatz = append(collatz, n)
    }
    sort.Slice(collatz, func(i, j int) bool {
        return collatz[i] < collatz[j]
    })
    var result []int
    for _, num := range collatz {
        if num%2 != 0 {
            result = append(result, num)
        }
    }
    return result
}
```