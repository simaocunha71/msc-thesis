To determine if a triangle is right-angled, it must satisfy the Pythagorean theorem,
which states that for a right-angled triangle the square of the length of the hypotenuse
(the side opposite the right angle) is equal to the sum of squares of the lengths of the
other two sides. In other words, the formula to determine if a triangle is a right-angled
triangle is:

hypotenuse^2 = side1^2 + side2^2

If the above equation is true, the triangle is a right-angled triangle. Otherwise, it is
not.

In the given problem, we are given the lengths of the three sides of the triangle. We can
check if the triangle is right-angled by checking if the equation holds true for the given
side lengths.

We can do this by calculating the square of the length of the hypotenuse and the sum of
squares of the lengths of the other two sides. If the square of the length of the hypotenuse is
equal to the sum of squares of the lengths of the other two sides, the triangle is a right-angled
triangle; otherwise, it is not.

Here is a code snippet that solves the problem:

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5))
    fmt.Println(RightAngleTriangle(1, 2, 3))
}
```

In the above code, the RightAngleTriangle function takes three integer parameters a, b, and c. It returns true if the three sides a, b, and c form a right-angled triangle; otherwise, it returns false.

The function checks if the square of the length of the hypotenuse (c*c) is equal to the sum of the squares of the lengths of the other two sides (a*a + b*b). If the equation holds true, the function returns true; otherwise, it returns false.

In the main function, we test the RightAngleTriangle function with two sets of side lengths.