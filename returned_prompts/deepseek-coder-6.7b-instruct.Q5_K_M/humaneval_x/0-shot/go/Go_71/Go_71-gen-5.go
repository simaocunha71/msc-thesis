The given program is written in Go programming language. It first checks if the sides form a valid triangle or not. If not, it returns -1. If so, it calculates the semi-perimeter of the triangle and then uses Heron's formula to calculate the area of the triangle. The area is rounded off to 2 decimal places.

The Heron's formula is used to calculate the area of a triangle given the length of all three sides. It states that the area of a triangle whose sides have lengths a, b, and c is sqrt[s(s - a)(s - b)(s - c)], where s is the semi-perimeter of the triangle given by s = (a + b + c) / 2.

The program uses the math package in Go to perform the square root operation. The area is multiplied by 100 and then rounded to the nearest integer before being divided by 100 to give the area to 2 decimal places.

Here's the Go code:

```go
package main

import (
    "fmt"
    "math"
)

func TriangleArea(a float64, b float64, c float64) interface{} {
    if (a + b <= c) || (b + c <= a) || (c + a <= b) {
        return -1
    }

    // calculate semi-perimeter
    s := (a + b + c) / 2

    // calculate area using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    return