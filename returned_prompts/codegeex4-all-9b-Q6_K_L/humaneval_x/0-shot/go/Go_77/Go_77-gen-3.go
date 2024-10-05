```go
func Iscube(a int) bool {
    if a == 0 {
        return true
    }
    root := int(math.Pow(math.Abs(float64(a)), 1.0/3.0))
    return root*root*root == a
}
```