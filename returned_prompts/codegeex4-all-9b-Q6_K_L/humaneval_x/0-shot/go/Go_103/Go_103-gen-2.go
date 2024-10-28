```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := float64(sum) / float64(m-n+1)
    roundedAvg := math.Round(avg)
    if roundedAvg > math.MaxInt32 || roundedAvg < math.MinInt32 {
        return -1
    }
    return fmt.Sprintf("0b%b", int(roundedAvg))
}
```
