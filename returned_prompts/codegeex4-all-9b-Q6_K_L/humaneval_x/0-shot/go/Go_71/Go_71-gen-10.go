```go
// Check if the three sides form a valid triangle
if a+b <= c || a+c <= b || b+c <= a {
    return -1
}

// Calculate the semi-perimeter of the triangle
s := (a + b + c) / 2

// Calculate the area of the triangle using Heron's formula
area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

// Round the area to 2 decimal points
area = math.Round(area*100) / 100

return area
```
