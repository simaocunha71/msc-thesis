```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the given sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter of the triangle
    s := (a + b + c) / 2

    // Calculate the area of the triangle using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    // Round the area to 2 decimal points
    roundedArea := math.Round(area*100) / 100

    return roundedArea
}
```

B:
```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the given sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter of the triangle
    s := (a + b + c) / 2

    // Calculate the area of the triangle using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    // Round the area to 2 decimal points
    roundedArea := math.Round(area*100) / 100

    // Return the rounded area
    return roundedArea
}
```

C:
```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the given sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter of the triangle
    s := (a + b + c) / 2

    // Calculate the area of the triangle using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    // Round the area to 2 decimal points
    roundedArea := math.Round(area*100) / 100

    // Return the rounded area as a float64
    return float64(roundedArea)
}
```

D:
```go
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the