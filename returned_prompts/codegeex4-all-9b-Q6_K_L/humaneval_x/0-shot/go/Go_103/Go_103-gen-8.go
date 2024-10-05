```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    avg := float64(n + m) / 2
    avgRounded := math.Round(avg)
    avgBinary := fmt.Sprintf("0b%b", int(avgRounded))
    return avgBinary
}
```