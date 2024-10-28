In order to determine whether three sides of a triangle can form a right-angled triangle, we can use the Pythagorean theorem. The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

In code, we can write a function called RightAngleTriangle that takes three integer arguments: a, b, and c, representing the lengths of the sides of a triangle. We can then use a conditional statement to check if the equation of the Pythagorean theorem holds true for the given values of a, b, and c. If the equation holds true, the function returns true; otherwise, it returns false.

Here is an example implementation of the RightAngleTriangle function in Go:

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5))  // true
    fmt.Println(RightAngleTriangle(1, 2, 3))  // false
}
```

In this example, the RightAngleTriangle function takes the side lengths 3, 4, and 5 as arguments and returns true because 3*3 + 4*4 equals 5*5. The function also takes the side lengths 1, 2, and 3 as arguments and returns false because 1*1 + 2*2 does not equal 3*3.

You can test the RightAngleTriangle function with different sets of side lengths to determine whether they can form a right-angled triangle.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
