    // check if triangle is valid
    if (a + b > c) && (a + c > b) && (b + c > a) {
        // calculate area
        s := (a + b + c) / 2
        area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
        return math.Round(area*100) / 100
    } else {
        return -1
    }
}
```

## Test cases

```go
func main() {
    fmt.Println(TriangleArea(3, 4, 5)) // 6.00
    fmt.Println(TriangleArea(1, 2, 10)) // -1
    fmt.Println(TriangleArea(3, 4, 5)) // 6.00
    fmt.Println(TriangleArea(7, 24, 25)) // 84.00
    fmt.Println(TriangleArea(3, 4, 10)) // -1
    fmt.Println(TriangleArea(1, 1, 1)) // 0.43
}
```

## Note

This code implements the Heron's formula to calculate the area of a triangle. It first checks if the lengths of the sides can form a valid triangle, and if so, calculates the area using Heron's formula. The area is then rounded to two decimal places before being returned. If the lengths cannot form a valid triangle, -1 is returned.

Heron's formula is a standard method for calculating the area of a triangle given the lengths of its three sides. It works by first calculating the semi-perimeter of the triangle (the sum of the lengths of the sides divided by 2), and then using this to calculate the area. The formula is derived from the angles of the triangle, but can be used without knowing these angles.

The area is calculated using the square root function (math.Sqrt), and the result is rounded to two decimal places using the rounding function (math.Round). The rounding function is used to ensure that the area is returned as a floating-point number rounded to two decimal places.