```go
func Iscube(a int) bool {
    root := math.Pow(float64(a), 1.0/3.0)
    return root == float64(int(root))
}
```