```go
func Iscube(a int) bool {
    if a < 0 {
        a = -a
    }
    root := int(math.Pow(float64(a), 1/3))
    return root*root*root == a
}
```