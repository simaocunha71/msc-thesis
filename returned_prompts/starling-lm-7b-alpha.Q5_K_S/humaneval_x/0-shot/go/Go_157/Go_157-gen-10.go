To determine whether a right-angled triangle can be formed, the sum of the squares of the two shorter sides should be equal to the square of the longest side.

Here's the step-by-step logic in solving this problem:

1. Calculate the sum of the squares of the two shorter sides (a^2 + b^2).
2. Calculate the square of the longest side (c^2).
3. Compare the two values. If they are equal, then it's a right-angled triangle.
4. Return true or false based on the comparison result.

Here's the implementation of the above logic:

```go
func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}
```

The time complexity of this function is O(1) as it performs a single comparison.


```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // Output: true
    fmt.Println(RightAngleTriangle(1, 2, 3)) // Output: false
}
```

```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // Output: true
    fmt.Println(RightAngleTriangle(1, 2, 3)) // Output: false
}
```







```go
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // Output: true
    fmt.Println(RightAngleTriangle(1,