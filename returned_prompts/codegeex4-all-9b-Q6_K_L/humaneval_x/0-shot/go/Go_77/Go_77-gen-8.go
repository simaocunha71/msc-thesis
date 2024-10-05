```go
func Iscube(a int) bool {
    if a < 0 {
        a = -a
    }
    root := int(math.Ceil(math.Pow(float64(a), 1.0/3.0)))
    return root*root*root == a
}
```