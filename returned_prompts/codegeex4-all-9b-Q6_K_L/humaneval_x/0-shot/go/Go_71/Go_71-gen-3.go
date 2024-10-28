```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter
    s := (a + b + c) / 2

    // Calculate the area using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    // Round the area to 2 decimal points
    area = math.Round(area*100) / 100

    return area
}
```
This solution checks if the given sides can form a valid triangle by comparing the sum of any two sides with the third side. If they can form a valid triangle, it calculates the area using Heron's formula and rounds it to 2 decimal points. If they cannot form a valid triangle, it returns -1. The solution is efficient and accurate.