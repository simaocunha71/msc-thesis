```go
func RightAngleTriangle(a, b, c int) bool {
    return (a*a + b*b == c*c) || (a*a + c*c == b*b) || (b*b + c*c == a*a)
}
```
