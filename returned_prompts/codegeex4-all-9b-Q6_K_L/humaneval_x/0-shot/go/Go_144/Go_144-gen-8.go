```go
import (
    "strconv"
    "strings"
)

// Your task is to implement a function that will Simplify the expression
// x * n. The function returns true if x * n evaluates to a whole number and false
// otherwise. Both x and n, are string representation of a fraction, and have the following format,
// <numerator>/<denominator> where both numerator and denominator are positive whole numbers.
// 
// You can assume that x, and n are valid fractions, and do not have zero as denominator.
// 
// Simplify("1/5", "5/1") = true
// Simplify("1/6", "2/1") = false
// Simplify("7/10", "10/2") = false
func Simplify(x, n string) bool {
    parts := strings.Split(x, "/")
    num1, _ := strconv.Atoi(parts[0])
    den1, _ := strconv.Atoi(parts[1])

    parts = strings.Split(n, "/")
    num2, _ := strconv.Atoi(parts[0])
    den2, _ := strconv.Atoi(parts[1])

    return (num1 * num2) % (den1 * den2) == 0
}
```
