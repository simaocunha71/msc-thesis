import (
    "math"
)

// Given the lengths of the three sides of a triangle. Return the area of
// the triangle rounded to 2 decimal points if the three sides form a valid triangle.
// Otherwise return -1
// Three sides make a valid triangle when the sum of any two sides is greater
// than the third side.
// Example:
// TriangleArea(3, 4, 5) == 6.00
// TriangleArea(1, 2, 10) == -1
func TriangleArea(a float64, b float64, c float64) interface{} {
    if (a+b+c) < 0 || (b+c < a && c+a < b) || (c+a < b && b+a < c) {
        return "Triangle invalid"
    } else {
        r := math.Sqrt(float64(math.Pow(b, 2) + float64(math.Pow(c, 2))))
        area := float64(math.Pow(r, -2)) / 2.0
        if !isnan(area) {
            return area
        } else {
            return "Triangle invalid"
        }
    }
}