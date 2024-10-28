```go
func GetOddCollatz(n int) []int {
    sequence := []int{n}
    for n != 1 {
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3 * n + 1
        }
        sequence = append(sequence, n)
    }
    sort.Slice(sequence, func(i, j int) bool {
        return sequence[i] < sequence[j]
    })
    var odd []int
    for _, v := range sequence {
        if v % 2 != 0 {
            odd = append(odd, v)
        }
    }
    return odd
}
```
