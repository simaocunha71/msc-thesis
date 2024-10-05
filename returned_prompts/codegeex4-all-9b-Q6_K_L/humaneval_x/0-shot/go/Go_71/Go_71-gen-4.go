```go
func TriangleArea(a float64, b float64, c float64) float64 {
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }
    s := (a + b + c) / 2
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
    return math.Round(area*100) / 100
}
```
This solution is correct and efficient. It checks if the given sides can form a valid triangle using the triangle inequality theorem. If the sides form a valid triangle, it calculates the area using Heron's formula and rounds it to two decimal points. Otherwise, it returns -1. This solution is concise and easy to understand.