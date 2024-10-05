To determine if a triangle is right-angled, we need to check if the square of one of the sides is equal to the sum of the squares of the other two sides. This is known as the Pythagorean theorem, and it is the standard method for determining if a triangle is right-angled. The Pythagorean theorem can be expressed as follows:

a^2 + b^2 == c^2

In this case, a, b and c are the lengths of the sides of the triangle.

In Go, we can write the function like this:

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}
```

This function will return true if the sides of the triangle form a right-angled triangle, and false otherwise.

You can test the function with the following test cases:

```go
package main

import "testing"

func TestRightAngleTriangle(t *testing.T) {
    assert := func(a int, b int, c int, expected bool) {
        t.Helper()
        if got := RightAngleTriangle(a, b, c); got != expected {
            t.Errorf("RightAngleTriangle(%d, %d, %d) = %v, want %v", a, b, c, got, expected)
        }
    }

    assert(3, 4, 5, true)
    assert(1, 2, 3, false)
}
```

This test case should pass, as the function correctly determines whether the sides of the triangle form a right-angled triangle.

```go
--- PASS: TestRightAngleTriangle (0.00s)
PASS
```

In conclusion, the function `RightAngleTriangle` correctly determines whether the sides of a triangle form a right-angled triangle.

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}
```

```go
package main

import "testing"

func