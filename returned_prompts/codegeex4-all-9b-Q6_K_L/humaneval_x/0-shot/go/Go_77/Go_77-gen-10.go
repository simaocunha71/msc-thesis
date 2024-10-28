```go
func Iscube(a int) bool {
    root := math.Pow(float64(a), 1/3)
    return math.Round(root) == root
}
```