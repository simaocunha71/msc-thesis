```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    return "0b" + fmt.Sprintf("%b", int(math.Round(float64(n+m)/2)))
}
```