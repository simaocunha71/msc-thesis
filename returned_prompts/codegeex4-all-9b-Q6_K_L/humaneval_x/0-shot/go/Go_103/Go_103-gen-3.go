```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    avg := float64(n + m) / 2.0
    roundedAvg := math.Round(avg)
    return fmt.Sprintf("0b%b", int(roundedAvg))
}
```