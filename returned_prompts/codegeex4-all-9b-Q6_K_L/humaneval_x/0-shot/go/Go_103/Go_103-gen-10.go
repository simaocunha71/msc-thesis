```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    return fmt.Sprintf("0b%b", int(math.Round(float64(n+m)/2)))
}
```