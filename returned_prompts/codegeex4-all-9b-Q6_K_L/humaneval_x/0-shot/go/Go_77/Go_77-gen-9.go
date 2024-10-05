```go
func Iscube(a int) bool {
    if a == 0 {
        return true
    }
    var x float64 = math.Abs(float64(a))
    var i float64 = math.Ceil(math.Pow(x, 1.0/3.0))
    return i*i*i == x
}
```