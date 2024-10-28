
func TriangleArea(a float64, h float64) float64 {
    return 0.5 * a * h
}

// Example usage:
fmt.Println(TriangleArea(5, 3))

Explanation:

The area of a triangle can be calculated by the formula: area = 0.5 * base * height. In this implementation, the function `TriangleArea` takes two parameters: the length of the triangle's base (`a`) and its height (`h`). Inside the function, the area is calculated by multiplying 0.5 by the base (`a`) and the height (`h`), and the result is returned.

To test the function, we can call it with sample values, such as `TriangleArea(5, 3)`. The function will calculate the area of the triangle with a base of 5 and a height of 3, and return the result. In this case, the area of the triangle is 7.5, so the output will be `7.5`.

By using the `fmt.Println` function, we can print the result to the console.

Overall, this implementation provides a simple way to calculate the area of a triangle given its base and height.

// Given length of a side and high return area for a triangle.
// >>> TriangleArea(5, 3)
// 7.5
func TriangleArea(a float64, h float64) float64 {
    return 0.5 * a * h
}

// Example usage:
fmt.Println(TriangleArea(5, 3))

Explanation:

The area of a triangle can be calculated by the formula: area = 0.5 * base * height. In this implementation, the function `TriangleArea` takes two parameters: the length of the triangle's base (`a`) and its height (`h`). Inside the function, the area is calculated by multiplying 0.5 by the base (`a`) and the height (`h`), and the result is returned.

To test the function, we can call it with sample values, such as `TriangleArea(5, 3)`. The function will calculate the area of the triangle with a base