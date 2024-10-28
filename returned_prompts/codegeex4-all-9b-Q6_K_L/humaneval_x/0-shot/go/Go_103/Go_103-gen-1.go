```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    avg := float64(n + m) / 2
    rounded := math.Round(avg)
    if rounded > math.MaxInt32 || rounded < math.MinInt32 {
        return -1
    }
    return fmt.Sprintf("0b%b", int(rounded))
}
```