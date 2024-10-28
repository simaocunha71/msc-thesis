```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }

    total := 0
    count := 0
    for i := n; i <= m; i++ {
        total += i
        count++
    }
    avg := float64(total) / float64(count)
    roundedAvg := int(math.Round(avg))

    return fmt.Sprintf("0b%b", roundedAvg)
}
```