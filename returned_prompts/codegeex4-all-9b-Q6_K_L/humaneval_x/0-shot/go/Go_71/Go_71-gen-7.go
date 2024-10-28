```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }
    s := (a + b + c) / 2
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
    return fmt.Sprintf("%.2f", area)
}
```