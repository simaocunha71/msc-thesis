```go
func GetOddCollatz(n int) []int {
    collatzSeq := []int{n}
    for n != 1 {
        if n%2 == 0 {
            n /= 2
        } else {
            n = 3*n + 1
        }
        collatzSeq = append(collatzSeq, n)
    }

    sort.Slice(collatzSeq, func(i, j int) bool {
        return collatzSeq[i]%2 != 0 && collatzSeq[j]%2 != 0 && collatzSeq[i] < collatzSeq[j]
    })

    return collatzSeq
}
```
