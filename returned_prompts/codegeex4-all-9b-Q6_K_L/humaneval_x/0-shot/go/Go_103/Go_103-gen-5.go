```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    roundedAvg := int(math.Round(float64(n+m)/2))
    return fmt.Sprintf("0b%b", roundedAvg)
}
```
