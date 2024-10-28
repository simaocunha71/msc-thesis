To determine if the sides of the triangle form a right-angled triangle, the sides should satisfy the Pythagorean theorem.

According to the Pythagorean theorem, for a triangle to be right-angled, the square of the length of the longest side should be equal to the sum of the squares of the lengths of the other two sides.

In other words, if we let `c` be the longest side, the condition for a right-angled triangle can be expressed as `c*c = a*a + b*b`.

To determine if the three sides of the triangle form a right-angled triangle, we should check if the above condition holds.

Here's a solution in Go:

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return c*c == a*a + b*b
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // true
    fmt.Println(RightAngleTriangle(1, 2, 3)) // false
}
```

The above code defines a function `RightAngleTriangle` that takes three integers as input, representing the lengths of the sides of a triangle, and returns a boolean value indicating whether the sides form a right-angled triangle.

The function checks if the square of the longest side (`c`) is equal to the sum of the squares of the other two sides (`a` and `b`). If the condition holds, the function returns `true`, otherwise it returns `false`.

The `main` function demonstrates the usage of the `RightAngleTriangle` function by calling it with two sets of side lengths and printing the result.

The output of the program will be:
```
true
false
```

This indicates that the first set of side lengths (3, 4, 5) form a right-angled triangle, while the second set of side lengths (1, 2, 3) do not.

In conclusion, to determine if the sides of a triangle form a right-angled triangle, you can use the Pythagorean theorem to check if the square of the longest side is equal to the sum of the squares of the